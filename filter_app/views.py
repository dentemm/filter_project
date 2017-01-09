import datetime
import csv


from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin

from . import models
from . import forms

# TESTS
class StatusMailView(TemplateView):

	template_name = 'statusmail.html'



# Create your views here.

class OverviewPage(ListView):

	model = models.Module
	context_object_name = 'module_list'
	template_name = 'overview.html'

	def get_queryset(self):

		return self.model.objects.all().prefetch_related('current_filter', 'previous_filter', 'recommended_filter', 'chemistry')

def overviewExport(request):

	response = HttpResponse(content_type='text/csv')


	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="overview.csv"'

	writer = csv.writer(response)

	writer.writerow(['Main Tool', 'Module', 'Current Filter', 'Previous Filter', 'Recommended Filter', 'Date Last Swap'])


	for module in models.Module.objects.all():

		tool = module.main_tool
		module_name = module.name
		current_filter = module.current_filter
		previous_filter = module.previous_filter
		recommended_filter = module.recommended_filter
		#chemistry = module.chemistry
		last_swap = module.last_swap

		writer.writerow([tool, module_name, current_filter, previous_filter, recommended_filter, last_swap])

	return response

class HistoryView(ListView):

	model = models.FilterSwap
	context_object_name = 'swap_list'
	template_name = 'overview2.html'

	def get_queryset(self):

		return self.model.objects.all().prefetch_related('module', 'swapped_filter', )

class OverdueView(ListView):

	model = models.Module
	context_object_name = 'overdue_list'
	template_name = 'overdue-view.html'

	def get_queryset(self):

		overdue_list = []

		for module in self.model.objects.all():

			if module.time_to_next_swap < 1:

				overdue_list.append(module)

		sorted_list = sorted(overdue_list, key=lambda t: -t.time_to_next_swap)

		return sorted_list

class ToolView(ListView):

	model = models.Tool
	context_object_name = 'tool_list'
	template_name = 'overview3.html'

	def get_context_data(self, **kwargs):

		modules = models.Module.objects.filter(main_tool__name__iexact=self.tool)

		ctx = super(ToolView, self).get_context_data(**kwargs)

		ctx['modules'] = modules
		ctx['current_tool'] = self.tool
		ctx['fab'] = self.fab

		return ctx

	def get_queryset(self):

		self.fab = self.kwargs['fab']

		if not self.kwargs['tool']:

			#print 'geen tool'
			self.tool = models.Tool.objects.filter(cleanroom__iexact=self.fab).first().name.lower()
			#print self.tool

		else:
			self.tool = self.kwargs['tool']

		return self.model.objects.filter(cleanroom__iexact=self.fab)

class ToolListSwapView(ListView):

	model = models.Tool
	context_object_name = 'tool_list'
	template_name = 'filterswap_form2.html'

	def get_queryset(self):

		#print list(self.model.objects.values_list('name', flat=True))

		return self.model.objects.values_list('name', flat=True)

class FilterDetailView(DetailView):

	model = models.Filter
	template_name = 'filter-details.html'
	context_object_name = 'filter'

class ModulesForToolSwapView(ListView):

	pass

class FormHandler(SuccessMessageMixin, CreateView):

	form_class = forms.SwapForm
	template_name = 'form-content.html'
	success_url = reverse_lazy('overview')
	success_message = 'Successfully added filter swap!'
	


	def get(self, request, *args, **kwargs):

		#print 'get'
		return super(FormHandler, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):

		print('post request: %s' % request)

		return super(FormHandler, self).post(request, *args, **kwargs)

	def form_valid(self, form):

		#print 'form valid'
		print form

		response = super(FormHandler, self).form_valid(form)

		response['temm'] = 'great'

		return response

	def form_invalid(self, form):

		#print 'form invalid'

		print('form errors: %s' % form.errors)

		response = super(FormHandler, self).form_invalid(form)

		response['temm'] = 'fail'

		return JsonResponse(request)

	def get_form_kwargs(self):

		#print 'get form kwargs van form handler'

		kwargs = super(FormHandler, self).get_form_kwargs()

		# 1. check if kwargs['tool'] exists
		tool = self.request.GET.get('tool', '')

		if tool == '':
			if self.request.session.get('tool', None):

				print 'session variable present!'
				tool = self.request.session['tool']

		else: 
			self.request.session['tool'] = tool
		
		#print 'tool= ' + tool

		kwargs['tool'] = tool

		return kwargs


class SwapCreateView(CreateView):
	
	#template_name = 'filterswap_form.html'
	template_name = 'form.html'
	success_url = reverse_lazy('')
	#model = models.FilterSwap
	#fields = '__all__'

	#tool = self.request.GET.get('tool', '')

	tools = []

	form_class = forms.SwapForm
	#form_class = forms.TestForm

	def get_context_data(self, **kwargs):

		self.tools = list(models.Tool.objects.values_list('name', flat=True))

		ctx = super(SwapCreateView, self).get_context_data(**kwargs)
		ctx['tools'] = self.tools

		return ctx


	def get_form_kwargs(self):

		print 'get form kwargs van swapcreateview'

		kwargs = super(SwapCreateView, self).get_form_kwargs()

		kwargs['tool'] = self.request.GET.get('tool', '')

		#print 'model form tool: ' + str(kwargs['tool'])

		return kwargs


	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt van swap'

class SwapUpdateView(UpdateView):
	
	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('')
	form_class = forms.SwapForm
	#form_class = forms.TestForm
	

class SwapDeleteView(DeleteView):

	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('history')
	#model = models.FilterSwap
	#fields = '__all__'

	form_class = forms.SwapForm
	#form_class = forms.TestForm


class HomeView(TemplateView):

	template_name = 'index.html'


class ModulesForToolView(ListView):

	model = models.Module
	context_object_name = 'module_list'
	template_name = 'tool-view-table-content.html'

	def get_queryset(self):
		return self.model.objects.values_list('name', flat=True)


'''Ajax handling views'''
class ModuleDetailView(DetailView):

	model = models.Module
	template_name = 'tool-view-detail-content.html'

	def get_context_data(self, **kwargs):

		ctx = super(ModuleDetailView, self).get_context_data(**kwargs)

		obj = ctx['object']

		if obj.last_swap != None:

			last_swap = obj.last_swap.date
			swap_time = obj.swap_interval * 30
			current_days = datetime.date.today() - last_swap

			if swap_time - current_days.days < 0:
				ctx['overdue'] = current_days.days - swap_time
				ctx['swap_remaining'] = 0

			else:
				ctx['swap_remaining'] = swap_time - current_days.days
				ctx['overdue'] = 0

			ctx['swap_passed'] = current_days.days
			
		return ctx
