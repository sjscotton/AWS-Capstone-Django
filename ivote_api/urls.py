from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voter', views.get_voter, name='get_voter'),

]
