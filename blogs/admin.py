from django.contrib import admin
from . import models


# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'description']
    list_editable = ['price', 'is_active']
    # readonly_fields = ['slug']
    prepopulated_fields = {'slug': ['title']}
    list_filter = ['is_active', 'price']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']
    list_editable = ['url_title']


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['color', 'Size']
    list_editable = ['Size']


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']


admin.site.register(models.Product, productAdmin)
admin.site.register(models.blogsCategory, ProductCategoryAdmin)
admin.site.register(models.ProductInformation, ProductInfoAdmin)
admin.site.register(models.ProductTag, ProductTagAdmin)
