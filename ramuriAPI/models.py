from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Brand(models.Model):
    """Fashion brand representation"""
    name = models.CharField(max_length=40)
    price_range = models.FloatField(blank=True, null=True)
    parent_company = models.CharField(blank=True, null=True, max_length=40)
    # url = models.CharField(max_length=40) 
    urls = ArrayField(models.CharField(max_length=100), default=list)
    goy_link = models.CharField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=100)

    # Good On You ratings, allowed blank, null
    planet_goy_rating = models.FloatField(blank=True, null=True)
    people_goy_rating = models.FloatField(blank=True, null=True)
    animal_goy_rating = models.FloatField(blank=True, null=True)

    # Fashion Transparency Index ratings, allowed blank, null
    policy_fti_rating = models.FloatField(blank=True, null=True)
    governance_fti_rating = models.FloatField(blank=True, null=True)
    knowshow_fti_rating = models.FloatField(blank=True, null=True)
    spotlight_fti_rating = models.FloatField(blank=True, null=True)
    traceability_fti_rating = models.FloatField(blank=True, null=True)


# class Scraper(models.Model):
#     """Representation for the """
    

