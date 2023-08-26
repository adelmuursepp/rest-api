from django.core.management.base import BaseCommand
from ramuriAPI.models import *

class Command(BaseCommand):
    help = 'Seeds data for the API'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # try:
        self.stdout.write('Cleaning data')
        Brand.objects.all().delete()
        self.stdout.write('Seeding brand data')
        self.create_brands()
        self.stdout.write(self.style.SUCCESS('Finished seeding data'))
    
    def create_brands(self):
        Brand.objects.create(name='Abercrombie and Fitch', price_range=0, urls=['abercrombie.com'], parent_company='Abercrombie & Fitch', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
            policy_fti_rating = 5.7, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
            spotlight_fti_rating = 1.2, traceability_fti_rating = 0.9, \
            goy_link='https://directory.goodonyou.eco/brand/abercrombie-and-fitch', location='United States')

        Brand.objects.create(name='Adidas', url='adidas.com', parent_company='Adidas Group', \
            planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
            policy_fti_rating = 9.1, governance_fti_rating = 6.2, knowshow_fti_rating = 4.9, \
            spotlight_fti_rating = 3.9, traceability_fti_rating = 5.8)

        Brand.objects.create(name='Aeropostale', url='aeropostale.com', parent_company='Adidas Group', \
            planet_goy_rating = 2.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
            policy_fti_rating = 1.7, governance_fti_rating = 0, knowshow_fti_rating = 0.6, \
            spotlight_fti_rating = 0, traceability_fti_rating = 0)
        
        Brand.objects.create(name='ALDI Nord', url='aldi-nord.com', parent_company='ALDI Einkauf GmbH & Co. oHG', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
            policy_fti_rating = 6.4, governance_fti_rating = 3.8, knowshow_fti_rating = 2.6, \
            spotlight_fti_rating = 1.4, traceability_fti_rating = 1.6)
        
        Brand.objects.create(name='ALDO', url='aldoshoes.com', parent_company='The Aldo Group Inc.', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
            policy_fti_rating = 4.4, governance_fti_rating = 1.5, knowshow_fti_rating = 2.1, \
            spotlight_fti_rating = 1, traceability_fti_rating = 0.1)
        
        Brand.objects.create(name='Amazon', url='amazon.com', parent_company='Amazon.com, Inc.', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
            policy_fti_rating = 7, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
            spotlight_fti_rating = 1.8, traceability_fti_rating = 2.2)
        
        Brand.objects.create(name='Amazon', url='amazon.com', parent_company='Amazon.com, Inc.', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
            policy_fti_rating = 7, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
            spotlight_fti_rating = 1.8, traceability_fti_rating = 2.2)

        Brand.objects.create(name='Zara', url='zara.com', parent_company='Inditex', \
            planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
            policy_fti_rating = 0, governance_fti_rating = 0, knowshow_fti_rating = 0, \
            spotlight_fti_rating = 0, traceability_fti_rating = 0)
