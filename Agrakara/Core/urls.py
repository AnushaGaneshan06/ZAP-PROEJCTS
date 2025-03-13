
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path("search/", views.search_districts, name="search_districts"),
    path('temples/', views.temple_list, name='temple_list'),


]