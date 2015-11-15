import datetime

from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy

from . import models
from . import forms

# Create your views here.

class OverviewPage(ListView):

	model = models.Module
	context_object_name = 'module_list'
	template_name = 'overview.html'

	def get_queryset(self):

		return self.model.objects.all().prefetch_related()

class HistoryView(ListView):

	model = models.FilterSwap
	context_object_name = 'swap_list'
	template_name = 'overview2.html'

	def get_queryset(self):

		return self.model.objects.all().prefetch_related()

class ToolView(ListView):

	model = models.Tool
	context_object_name = 'tool_list'
	template_name = 'overview3.html'

	def get_context_data(self, **kwargs):

		modules = models.Module.objects.filter(main_tool__name__iexact=self.tool).prefetch_related()

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

		return self.model.objects.filter(cleanroom__iexact=self.fab).prefetch_related()

class ToolListSwapView(ListView):

	model = models.Tool
	context_object_name = 'tool_list'
	template_name = 'filterswap_form2.html'

	def get_queryset(self):

		print list(self.model.objects.values_list('name', flat=True))

		return self.model.objects.values_list('name', flat=True)

class ModulesForToolSwapView(ListView):

	pass

class FormHandler(CreateView):

	template_name = 'form-content.html'
	success_url = reverse_lazy('overview')

	form_class = forms.SwapForm
	#form_class = forms.TestForm


	def clean(self):

		print 'clean'

	def form_valid(self, form):

		print 'form valid'
		print form

		return super(FormHandler, self).form_valid(form)

	def form_invalid(self, form):

		print 'form invalid'

	def get_form_kwargs(self):

		print 'get form kwargs van form handler'

		kwargs = super(FormHandler, self).get_form_kwargs()

		kwargs['tool'] = self.request.GET.get('tool', '')

		#print 'model form tool: ' + str(kwargs['tool'])

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

		print 'model form tool: ' + str(kwargs['tool'])

		return kwargs


	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt van swap'

class SwapUpdateView(UpdateView):
	
	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('')
	form_class = forms.SwapForm
	#form_class = forms.TestForm
	

	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt'

class SwapDeleteView(DeleteView):

	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('history')
	#model = models.FilterSwap
	#fields = '__all__'

	form_class = forms.SwapForm
	#form_class = forms.TestForm

	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt'

class HomeView(TemplateView):

	template_name = 'index.html'


class ModulesForToolView(ListView):

	model = models.Module
	context_object_name = 'module_list'
	template_name = 'tool-view-table-content.html'

	def get_queryset(self):

		#print list(self.model.objects.values_list('name', flat=True))

		return self.model.objects.values_list('name', flat=True)


'''Ajax handling views'''
class ModuleDetailView(DetailView):

	model = models.Module
	template_name = 'tool-view-detail-content.html'

	def get_context_data(self, **kwargs):

		ctx = super(ModuleDetailView, self).get_context_data(**kwargs)

		obj = ctx['object']

		last_swap = obj.last_swap.date
		swap_time = obj.swap_interval * 365
		current_days = datetime.date.today() - last_swap

		ctx['swap_passed'] = current_days.days
		ctx['swap_remaining'] = swap_time - current_days.days

		return ctx




