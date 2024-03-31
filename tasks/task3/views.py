from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .renderers import CustomAesRenderer
from .serializers import ProductSerializer
from .models import Product

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .renderers import AES_SECRET_KEY, AES_IV
import json


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductSerializer(products, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductEncryptedView(APIView):
    renderer_classes = [CustomAesRenderer]

    def get(self, request):
        products = Product.objects.all()
        if products:
            serializer = ProductSerializer(products, many=True)
            data = serializer.data
        data = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'data': data
        }
        return Response(data, status=status.HTTP_200_OK)


class ProductDecryptView(APIView):
    def post(self, request, *args, **kwargs):
        if 'ciphertext' not in request.data:
            return Response({
                                "error": "Missing 'ciphertext' field. Encrypt qilganda olgan shifrni kiritish orqali deshifrlash mumkun."},
                            status=status.HTTP_400_BAD_REQUEST)

        encrypted_data = request.data['ciphertext']
        enc = base64.b64decode(encrypted_data)
        cipher = AES.new(AES_SECRET_KEY, AES.MODE_CBC, AES_IV)
        try:
            decrypted_data = unpad(cipher.decrypt(enc), 16)
            decrypted_data = json.loads(decrypted_data)
            data = {
                "data": decrypted_data
            }
            return Response(data)
        except Exception as e:
            return Response({"data": f"An error- {e}"})


class ProductCreate(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

