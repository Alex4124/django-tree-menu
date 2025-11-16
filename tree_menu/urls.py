from django.urls import path, re_path
from . import views

app_name = 'tree_menu'

urlpatterns = [
    path('', views.universal_page, name='home'),
    path('about/', views.universal_page, name='about'),
    path('contacts/', views.universal_page, name='contacts'),
    path('services/', views.universal_page, name='services'),
    
    re_path(r'^.*/$', views.universal_page),
]