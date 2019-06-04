from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),      # utils/
    path('art/<str:keyword>/', views.artii),     # utils/art/<keyword>
    path('stock_input/', views.stock_input),
    path('stock_output/', views.stock_output),
]
