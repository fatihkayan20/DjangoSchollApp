from django.urls import path
from . import views

app_name='anasayfa'
urlpatterns = [
    path('',views.index,name='index'),
]
