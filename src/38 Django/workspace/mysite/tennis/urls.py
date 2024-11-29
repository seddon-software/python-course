from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /filter/

    #firefox 'http://localhost:7000/tennis/filter/Blue?a=9&b=3'
    path('filter/<team>/', views.filter, name='filter'),

    # ex: /results/
    path('<str:team>/results/', views.results, name='results'),
    # ex: /tennis/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('f1/<param1>/<param2>/', views.f1, name='f1'),

    # firefox 'http://localhost:7000/tennis/f2/'
    path('f2/', views.f2, name='f2'),
    
    # firefox 'http://localhost:7000/tennis/f3/'
    path('f3/', views.f3, name='f3'),
]
