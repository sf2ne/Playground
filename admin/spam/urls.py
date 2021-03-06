from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SpamList.as_view(), name='spam'),
    url(r'^(?P<spam_id>[a-z0-9]+)/$', views.SpamDetail.as_view(), name='detail'),
    url(r'^(?P<spam_id>[a-z0-9]+)/email/$', views.email, name='email'),
]
