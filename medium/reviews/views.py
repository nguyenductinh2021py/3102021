from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer, ImageSerializer
from .models import Product, Image
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
