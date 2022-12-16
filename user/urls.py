from django.urls import path
from . import views

urlpatterns = [
    # path('tradd/', views.tr_create_view, name='tr_add'),
    path('', views.tr_home, name='tr_home'),
    path('add/', views.tr_add, name='tr_add')
    
]
