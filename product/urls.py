from django.urls import path
from .import views

app_name = "product"

urlpatterns = [
    path('', views.product_type, name='product_type'),
    path('list/<str:category>/', views.product_list, name='product_list'),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),

]

