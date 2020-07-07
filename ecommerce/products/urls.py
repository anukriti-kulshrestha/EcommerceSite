from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductIndex.as_view(), name='product'),
    path('<int:prod_id>/',views.product_details,name='prod_details'),
    path('cart/',views.add_to_cart,name='addtocart'),
]