from django.contrib import admin
from django.urls import path
from accounts.views import *


urlpatterns = [   
    
    path('signup/',registra_usuario, name= 'signup'),
    path('login/',login_request, name='login'),
    path('logout/',logout_request, name='logout'),
    path('profile/<username>',profile , name='profile'),
    path('edit_profile/',edit_profile, name='edit_profile'),
    path('editar_usuario/',editar_usuario, name='editar_usuario'),
    path('post/<int:pk>',ArticleDetailView.as_view(), name= 'post_details'),
]
