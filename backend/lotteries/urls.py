from django.urls import path

from . import views


app_name = 'lotteries'
urlpatterns = [
    path('', views.EventListView.as_view(), name='events'),
    path('<str:pk>/detail', views.EventDetailView.as_view(), name='event_detail'),
    path('register', views.register, name='register'),
    path('participants', views.participants, name='participants'),
    path('ballots/submit', views.submit, name='submit'),
]