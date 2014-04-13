from django.conf.urls import patterns, url
from django.views.generic import list_detail
from questions import views
from questions.models import Questions, Comments

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
)
