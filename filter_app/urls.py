from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.OverviewPage.as_view(), name='overview'),
	url(r'history/$', views.HistoryView.as_view(), name='history'),
	url(r'^tools/$', views.ToolView.as_view(), name='tools'),

	url(r'^tools/(?P<fab>[\w-]+)/(?P<tool>[\w-]*)$', views.ToolView.as_view(), name='test'),
]