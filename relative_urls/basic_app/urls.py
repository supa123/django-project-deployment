from django.conf.urls import url
from . import views

app_name='basic_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),

]
