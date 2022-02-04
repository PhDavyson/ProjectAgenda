from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.acessar_contato, name='acessar_contato'),
]
