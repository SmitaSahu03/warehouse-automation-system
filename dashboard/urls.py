from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.index,name = 'dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('product/',views.product,name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update,name='dashboard-product-update'),
    path('rack/',views.rack,name='dashboard-rack'),
    
]