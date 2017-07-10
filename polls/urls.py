from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^list_the_files/$',views.list_the_files,name="list"),
    url(r'^delete_files/$',views.delete_files,name="delete"),
]