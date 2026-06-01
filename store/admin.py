from django.contrib import admin

from .models import Category, Manufacturer, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
	list_display = ['name', 'country', 'slug']
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'category', 'manufacturer', 'price', 'stock', 'featured']
	list_filter = ['featured', 'category', 'manufacturer']
	search_fields = ['name', 'short_description', 'description']
	prepopulated_fields = {'slug': ('name',)}
