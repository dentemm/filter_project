from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.OverviewPage.as_view(), name='overview'),
	url(r'history/$', views.HistoryView.as_view(), name='history'),
	url(r'^tools/$', views.ToolView.as_view(), name='tools'),
	url(r'^new/$', views.SwapCreateView.as_view(), name='new-swap'),
	url(r'^formtest/$', views.FormHandler.as_view(), name='form-handler'),

	url(r'^filter/(?P<pk>[\w-]+)/$', views.FilterDetailView.as_view(), name='filter-detail'),

	url(r'^new/test/$', views.ToolListSwapView.as_view(), name='test'),

	url(r'^latest/(?P<tool>[\w-]+)/$', views.ModulesForToolView.as_view(), name='modules-for-tool'),


	url(r'^tools/(?P<fab>[\w-]+)/(?P<tool>[\w-]*)$', views.ToolView.as_view(), name='test'),

	url(r'^index/$', views.HomeView.as_view(), name='home'),


	url(r'^ajax/(?P<pk>[\w-]+)/$', views.ModuleDetailView.as_view(), name='module-detail'),
]