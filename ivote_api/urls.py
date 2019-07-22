from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voter', views.get_voter, name='get_voter'),
    path('vote_dates', views.get_votes, name='get_votes'),
    path('stats', views.get_stats, name='get_stats'),
    # path('reps', views.get_reps, name='get_reps'),

]
