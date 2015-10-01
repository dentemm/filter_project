from django.forms import ModelForm, ModelChoiceField


from .models import FilterSwap, Module

class SwapForm(ModelForm):

	def __init__(self, tool, *args, **kwargs):

		super(SwapForm, self).__init__(*args, **kwargs)

		#tool = self.request.GET.get('tool', '')
		print "here: " + str(tool)
		self.fields['module'] = ModelChoiceField(queryset=Module.objects.filter(main_tool__name__iexact=tool))


	class Meta:
		model = FilterSwap
		#fields = ['module', 'swapped_filter', 'comment', 'date', 'who']
		fields = '__all__'
