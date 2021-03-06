from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from bligress import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
     url(r'^login/$', views.loginview, name='login'),
     url(r'^logout/$', views.logoutview, name='logout'),
     url(r'^kanban/', include('kanban.urls', namespace="kanban")),
     url(r'^admin/', include(admin.site.urls)),
)
