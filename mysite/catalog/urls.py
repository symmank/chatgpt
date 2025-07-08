from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('form/<int:pk>/', views.contact_form, name='contact_form'),
]
