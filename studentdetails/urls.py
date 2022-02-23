from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name = 'index'),
    path('all',views.all,name='all'),
    path('rec_data',views.rec_data,name='rec_data'),


]