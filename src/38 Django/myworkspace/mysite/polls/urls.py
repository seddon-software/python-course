from django.urls import path

from . import views

urlpatterns = [
    # ex: /tennis/
    path('', views.index, name='index'),
    # ex: /detail/
    path('<str:team>/', views.detail, name='detail'),
    # ex: /results/
    path('<str:team>/results/', views.results, name='results'),
    # ex: /tennis/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
