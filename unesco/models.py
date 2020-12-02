from django.db import models
# Create your models here.

class States(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey('Region',on_delete=models.CASCADE)

class Region(models.Model):
    name = models.CharField(max_length=200)

class Site(models.Model):

    name            = models.CharField(max_length=200)
    year            = models.IntegerField(null=True)
    description     = models.TextField(null=True)
    justification   = models.TextField(null=True)
    longitude       = models.FloatField(null=True)
    latitude        = models.FloatField(null=True)
    area_hectares   = models.FloatField(null=True)
    category        = models.ForeignKey('Category',on_delete=models.CASCADE)
    state           = models.ForeignKey('States',on_delete=models.CASCADE)
    iso             = models.ForeignKey('Iso',on_delete=models.CASCADE)

class Iso(models.Model):
    name = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200)