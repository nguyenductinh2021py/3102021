from django.contrib import admin
from .models import Product, Category, Company, ProductSize, ProductSite, Comment
from .models import Image

admin.site.register(Image)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')
    list_filter = ('category', )

#admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Comment)