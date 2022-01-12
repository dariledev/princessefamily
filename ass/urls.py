from django.urls import path 


from .import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('details/', views.detail, name='detail'),
    path('cree_your_account/', views.register, name='register'),
    path('espace_don/', views.donateur, name='don'),
    path('projets/', views.projets, name='projets'),
    path('projets_don/', views.projets_don, name='projets_don'),
    path('celibat/', views.celibat, name='celibat'),
    path('error/', views.error, name='error'),
    path('ajouter/', views.add, name='add'),
    path('login/', views.login_user, name='login'),
    path('checkout/', views.payement, name='payement'),


    









]