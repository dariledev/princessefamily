from django.urls import path 


from .import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('deatil/', views.detail, name='detail'),
    path('cree_your_account/', views.register, name='register'),
    path('espace_don/', views.donateur, name='don'),



]