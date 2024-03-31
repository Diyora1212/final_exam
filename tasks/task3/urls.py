from django.urls import path
from . import views
from .views import ProductView, ProductEncryptedView, ProductDecryptView, ProductCreate

urlpatterns = [
    path('product/', ProductView.as_view(), name='product-cypher'),
    path('product-encr/', ProductEncryptedView.as_view(), name='encrypt-product'),
    path('product-decr/', ProductDecryptView.as_view(), name='decrypt-product'),
    path('product-create/', ProductCreate.as_view(), name='product-create')

]