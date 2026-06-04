from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Назва товару")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Зображення")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")
    available = models.BooleanField(default=True, verbose_name="В наявності")
    rating = models.PositiveIntegerField(default=5, verbose_name="Рейтинг (від 1 до 5)")

    def __str__(self):
        return self.name

    @property
    def stars_html(self):
        safe_rating = min(max(self.rating, 0), 5)
        return '★' * safe_rating + '☆' * (5 - safe_rating)
    
