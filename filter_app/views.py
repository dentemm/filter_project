from django.views.generic import ListView, TemplateView

from . import models

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
		self.tool = self.kwargs['tool']

		return self.model.objects.filter(cleanroom__iexact=self.fab).prefetch_related()