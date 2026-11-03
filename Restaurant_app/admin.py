from django.contrib import admin
from Restaurant_app.models import FoodCategoryDb, FoodDb

# Register your models here.

admin.site.register(FoodCategoryDb)
admin.site.register(FoodDb)