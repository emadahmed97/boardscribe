from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<article_id>[0-99]+)/$', views.detail, name='detail')

]
