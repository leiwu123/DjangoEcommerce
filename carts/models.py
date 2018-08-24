from django.conf import settings
from django.db import models

from products.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
  def new(self, user=None):
    user_obj = None
    # print(user)
    if user is not None:
      # print(user.username)
      if user.is_authenticated():
        user_obj = user
    return self.model.objects.create(user=user_obj)

# Create your models here.
class Cart(models.Model):
  user = models.ForeignKey(User, null=True, blank=True)
  products = models.ManyToManyField(Product, blank=True)
  total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)

  objects = CartManager()

  def __str__(self):
    return str(self.id)