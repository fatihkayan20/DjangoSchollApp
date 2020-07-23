from django.urls import path
from . import views

app_name='foto'
urlpatterns = [
    path('', views.index,name='index'),
    path('<int:id>', views.fullscreenFoto, name='fullscreenFoto'),
    path('<slug:slug>', views.detail,name='detail'),
]
