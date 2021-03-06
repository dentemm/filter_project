from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.OverviewPage.as_view(), name='overview'),
	url(r'^export/$', views.overviewExport, name='overview-export'),

	url(r'history/$', views.HistoryView.as_view(), name='history'),
	url(r'^tools/$', views.ToolView.as_view(), name='tools'),
	url(r'^new/$', views.SwapCreateView.as_view(), name='new-swap'),
	url(r'^overdue/$', views.OverdueView.as_view(), name='overdue'),
	url(r'^formtest/$', views.FormHandler.as_view(), name='form-handler'),

	url(r'^filter/(?P<pk>[\w-]+)/$', views.FilterDetailView.as_view(), name='filter-detail'),

	url(r'^new/test/$', views.ToolListSwapView.as_view(), name='test'),

	url(r'^latest/(?P<tool>[\w-]+)/$', views.ModulesForToolView.as_view(), name='modules-for-tool'),


	url(r'^tools/(?P<fab>[\w-]+)/(?P<tool>[\w-]*)$', views.ToolView.as_view(), name='test'),

	url(r'^index/$', views.HomeView.as_view(), name='home'),


	url(r'^ajax/(?P<pk>[\w-]+)/$', views.ModuleDetailView.as_view(), name='module-detail'),

	# TESTS
	url(r'^statusmail/$', views.StatusMailView.as_view(), name='statusmail')
]