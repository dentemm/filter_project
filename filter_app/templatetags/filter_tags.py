from django import template
from django.core.urlresolvers import resolve

register = template.Library()

class ActiveUrlNode(template.Node):
    def __init__(self, request, names, return_value='active'):
        self.request = template.Variable(request)
        #self.names = [template.Variable(n) for n in names]
        self.names = names
        self.return_value = template.Variable(return_value)

        print 'names' + str(self.names)

    def render(self, context):
        request = self.request.resolve(context)
        any_of = False
        try:
            url = resolve(request.path_info)

            print 'url: ' + str(url.url_name)

            url_name = url.url_name

            print 'url name-- ' + str(url_name)
            print 'den andere-- ' + str(self.names)

            if url_name == self.names:
                print 'jeeeeej'
                any_of=True

            else:
                print 'tis ni waar '

            '''for n in self.names:
                name = n.resolve(context)
                if url_name.startswith(name):
                    any_of = True
                    break'''
        except:
            # TODO - think a better way to log these
            print "Cannot resolve %s" % request.path_info
        return self.return_value if any_of else ''

@register.tag
def active(parser, token):
    """
        Simple tag to check which page we are on, based on resolve;
        Useful to add an 'active' css class in menu items that needs to be
        aware when they are selected.

        Usage:

            {% active request "base:index" %}
            {% active request "base:index" "base:my_view" %}
    """
    try:
        args = token.split_contents()

        print 'args: ' + str(args[1]) + ' ' + str(args[2])

        #return ActiveUrlNode(args[1], args[2:])
        return ActiveUrlNode(args[1], args[2])
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires at least 2 arguments" % token.contents.split()[0]