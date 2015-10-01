from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
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

	def get_queryset(self):

		print list(self.model.objects.values_list('name', flat=True))

		return self.model.objects.values_list('name', flat=True)

class ModulesForToolSwapView(ListView):

	pass


class SwapCreateView(CreateView):
	
	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('')
	#model = models.FilterSwap
	#fields = '__all__'

	form_class = forms.SwapForm

	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt'

class SwapUpdateView(UpdateView):
	
	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('')
	#model = models.FilterSwap
	#fields = '__all__'

	form_class = forms.SwapForm

	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt'

class SwapDeleteView(DeleteView):

	template_name = 'filterswap_form.html'

	success_url = reverse_lazy('history')
	#model = models.FilterSwap
	#fields = '__all__'

	form_class = forms.SwapForm

	def post(self, request, *args, **kwargs):

		print 'in post methode geraakt'


