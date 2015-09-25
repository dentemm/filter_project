from django.views.generic import ListView

from . import models

# Create your views here.

class OverviewPage(ListView):

	model = models.Module
	context_object_name = 'module'
	template_name = 'overview.html'

	def get_queryset(self):

		return self.model.objects.all().prefetch_related()