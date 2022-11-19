from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class ListingManager(models.Manager):
    def get_queryset(self):
        return super(ListingManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    """Model for listing categories"""
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('listing:category_list', args=[self.slug])
    
    def __str__(self):
        return self.name

class Listing(models.Model):
    """Model for Products and their details"""
    category = models.ForeignKey(Category, related_name='product', 
    on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/static', default='images/back.png')
    price = models.DecimalField(max_digits=19, decimal_places=2)
    date_created= models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, 
    related_name='product_creator')
    slug = models.SlugField(max_length=255)
    is_active = models.BooleanField(True)
    auctioned = models.BooleanField(False)
    objects = models.Manager()
    listings=ListingManager()


    class Meta:
        verbose_name_plural = 'Listings'
        ordering = ('-date_created', )

    def get_absolute_url(self):
        return reverse('listing:item_detail', args=[self.slug])

    def __str__(self):
        return self.item

class ListingBid(models.Model):
    """
    Model for Bids for all products
    """
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bids = models.IntegerField(blank=True, null=True) 
    bidders = models.ManyToManyField(User, blank=True, related_name='bidders')

    class Meta:
        verbose_name_plural = 'ListingBids'
    

    
