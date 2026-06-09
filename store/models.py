from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(max_length=140, unique=True)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
		ordering = ['name']

	def __str__(self):
		return self.name


class Manufacturer(models.Model):
	name = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(max_length=140, unique=True)
	country = models.CharField(max_length=80, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=160)
	slug = models.SlugField(max_length=180, unique=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')
	short_description = models.CharField(max_length=240)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField(default=0)
	featured = models.BooleanField(default=False)
	image = models.ImageField(upload_to='products/', blank=True, null=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_detail', kwargs={'slug': self.slug})
