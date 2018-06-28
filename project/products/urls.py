from django.urls import path
from django.conf.urls import url
from .views import list_products,create_products,update_products,delete_products

urlpatterns=[
    path('',list_products,name = 'all-products'),
    path('new',create_products,name = 'create_product'),
    path('update/<int:id>/',update_products,name = 'update_products'),
    path('delete/<int:id>/',delete_products,name = 'delete_products'),
]
