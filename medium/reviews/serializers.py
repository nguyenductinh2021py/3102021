from .models import Product, Comment
from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import Image
from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(sizes=[('full_size', 'url'), ('thumbnail', 'thumbnail_100x100'),])
    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'updated']
        expandable_fields = {
            'category' : ('reviews.CategorySerializer', {'many': True}),
            'sites': ('reviews.ProductSiteSerializer', {'many': True}),
            'comments': ('reviews.CommentSerializer', {'many': True}),
            'image': ('reviews.ImageSerializer', {'many': True}),
        }
    
