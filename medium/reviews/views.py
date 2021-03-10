from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product
from .models import Image

class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
  