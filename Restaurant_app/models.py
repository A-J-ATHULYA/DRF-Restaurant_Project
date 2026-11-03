from django.db import models

# Create your models here.

class FoodCategoryDb(models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.category_name
    
class FoodDb(models.Model):
    category = models.ForeignKey(FoodCategoryDb, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=300)
    price= models.DecimalField(max_digits=10, decimal_places=3)
    ingredients = models.TextField()
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name