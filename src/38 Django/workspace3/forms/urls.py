from django.urls import path

from . import views

urlpatterns = [
    # called from the template: action = /forms/printResults/'
    path('printResults/', views.printResults, name='printResults'),

    # firefox 'http://localhost:7000/forms/home/'
    path('home/', views.homeView, name='homeView'),
]
