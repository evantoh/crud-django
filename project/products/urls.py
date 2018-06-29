from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path('',views.list_products,name = 'all-products'),
    path('new',views.create_products,name = 'create_product'),
    path('update/<int:id>/',views.update_products,name = 'update_products'),
    path('delete/<int:id>/',views.delete_products,name = 'delete_products'),
]
