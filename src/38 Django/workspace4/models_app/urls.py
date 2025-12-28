from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.resultsView, name='resultsView'),
]
