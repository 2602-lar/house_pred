from django.db import models

# Create your models here.
class Property(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    stories = models.IntegerField()
    mainroad = models.BooleanField()
    guestroom = models.BooleanField()
    basement = models.BooleanField()
    hotwaterheating = models.BooleanField()
    airconditioning = models.BooleanField()
    parking = models.IntegerField()
    prefarea = models.BooleanField()
    furnishingstatus = models.CharField(max_length=255)
    predictedprice = models.IntegerField()
    