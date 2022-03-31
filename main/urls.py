from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', generic, name ='category'),
    path('apt_detail/<int:pk>/', detail_kv, name='detail'),
    path('add_information/', add_information, name='add-information'),
]
