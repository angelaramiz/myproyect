from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10,decimal_places=2)
    image_url = models.URLField()
    description = models.TextField()
    comments = models.FileField()
    related_products = models.ManyToManyField('self',blank=True)

    def __str__(self):
        return self.name
