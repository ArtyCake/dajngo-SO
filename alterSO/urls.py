from django.conf.urls import patterns, include, url

from django.contrib import admin

from questions.views import QuestionsList, QuestionDetailView, QuestionCreate

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alterSO.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^registration/', include('registration.backends.default.urls')),
    # url(r'^questions/', include('questions.urls', namespace="questions")),
    url(r'^questions/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question-detail'),
    url(r'^questions/create/$', QuestionCreate.as_view()),
    url(r'^questions/', QuestionsList.as_view()),

    url(r'^admin/', include(admin.site.urls)),
)
