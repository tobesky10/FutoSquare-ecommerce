from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50, null=True)
    phone_number = models.PositiveBigIntegerField(null=True)
    avatar = models.ImageField(upload_to='profiles/', null=True, default='avatar.svg')
    # gender = models.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=60)
    product_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    product_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    product_image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=30)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='category_products')

    def __str__(self):
        return self.name


class Message(models.Model):
    RATING_CHOICES = (('1 ', '1 Star'),
                      ('2 ', '2 Stars'),
                      ('3 ', '3 Stars'),
                      ('4 ', '4 Stars'),
                      ('5 ', '5 Stars')
                      )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=100, blank=True)
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.user)

