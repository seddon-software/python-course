from django.urls import path

from . import views

urlpatterns = [
    # firefox 'http://localhost:7000/multiple_views'
    path('', views.index, name='index'),

    #firefox 'http://localhost:7000/multiple_views/view1'
    path('view1/', views.view1, name='view1'),

    #firefox 'http://localhost:7000/multiple_views/view2/abc/def'
    path('view2/<param1>/<param2>/', views.view2, name='view2'),

    #firefox 'http://localhost:7000/multiple_views/view3'
    path('view3/', views.view3, name='view3'),
]
