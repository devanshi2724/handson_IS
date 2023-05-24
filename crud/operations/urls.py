from django.contrib import admin
from django.urls import path
from operations import views
from .views import incubator_list


urlpatterns = [
        path('', views.home, name='home'),
        path('create-book/', views.create_book, name='create_book'),
        path('create-incubator/', views.new_incubator, name='new_incubator'),
        path('incubator-list/', views.incubator_list, name='incubator_list'),
]