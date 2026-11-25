# blog\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                              # Rota para a página inicial
    path('contacts/' , views.contacts, name='contacts'),            # Rota para página de contatos 
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Página do post completo
    path('login/', views.login_view, name='login'),                 # Login do usuário
    path('profile/', views.profile, name='profile'),                # Perfil do usuário logado
]