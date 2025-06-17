from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Makes sure no product can be added twice
        unique_together = ('user', 'product')

    def __str__ (self):
        return f"{self.user.username} {self.product.name}"