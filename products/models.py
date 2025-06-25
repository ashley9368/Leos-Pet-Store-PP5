from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    @property
    def upvotes(self):
        #Count how many upvotes this products has
        return self.votes.filter(vote_type=ProductVote.UP).count()

    @property
    def downvotes(self):
        #Count how many downvotes this products has
        return self.votes.filter(vote_type=ProductVote.DOWN).count()

    @property
    def is_flagged(self):
        #If there is more then 4 downvotes mark this product as flagged, then show red border for superuser
        return self.downvotes >= 4

#Keep track of each user's up/down vote
class ProductVote(models.Model):
    UP = 'U'
    DOWN = 'D'
    VOTE_CHOICES = [
        (UP, 'Upvote'),
        (DOWN, 'Downvote'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=1, choices=VOTE_CHOICES)

    class Meta:
        #Stop the user from voting twice on one product
        unique_together = ('product', 'user')

"""Review System models"""
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.ImageField(upload_to='review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.product.name}"