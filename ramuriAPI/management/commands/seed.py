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

        Brand.objects.create(name='Abercrombie and Fitch', price_range=2.0, urls=['abercrombie.com'], parent_company='Abercrombie & Fitch',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.7, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/abercrombie-and-fitch', location='United States')

                

        Brand.objects.create(name='Adidas', price_range=2.0, urls=['adidas.com', 'adidas.ca'], parent_company='Adidas Group',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.1, governance_fti_rating = 6.2, knowshow_fti_rating = 4.9, \
                spotlight_fti_rating = 3.9, traceability_fti_rating = 5.8, \
                goy_link='https://directory.goodonyou.eco/brand/adidas', location='Germany')

        Brand.objects.create(name='Aeropostale', price_range=2.0, urls=['aeropostale.com', 'blnts.com'], parent_company='SPARC Group LLC',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.7, governance_fti_rating = 0.0, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/aeropostale', location='United States')

        Brand.objects.create(name='ALDI Nord', price_range=0, urls=['aldi-nord.com', 'aldi-nord.de'], parent_company='ALDI Einkauf GmbH & Co. oHG',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.8, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 1.4, traceability_fti_rating = 1.6, \
                goy_link='https://directory.goodonyou.eco/brand/aldi', location='')

        Brand.objects.create(name='ALDO', price_range=2.0, urls=['aldoshoes.com'], parent_company='The Aldo Group Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.4, governance_fti_rating = 1.5, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.0, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/aldo', location='Canada')

        Brand.objects.create(name='Amazon', price_range=2.0, urls=['amazon.com'], parent_company='Amazon.com, Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 2.2, \
                goy_link='https://directory.goodonyou.eco/brand/amazon', location='United States')

        Brand.objects.create(name='American Eagle', price_range=2.0, urls=['ae.com'], parent_company='Retail Ventures',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.7, governance_fti_rating = 3.8, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/american-eagle', location='United States')

        Brand.objects.create(name='ANTA', price_range=2.0, urls=['anktshop.com'], parent_company='Anta International Group Holdings Ltd.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.3, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/anta', location='China')

        Brand.objects.create(name='Anthropologie', price_range=3.0, urls=['anthropologie.com'], parent_company='Urban Outfitters',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.0, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/anthropologie', location='United States')

        Brand.objects.create(name='Aritzia', price_range=3.0, urls=['aritzia.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.0, governance_fti_rating = 6.2, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 2.0, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/aritzia', location='Canada')

        Brand.objects.create(name='Armani', price_range=4.0, urls=['armani.com'], parent_company='Giorgio Armani S.p.A',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.6, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/giorgio-armani', location='United States')

        Brand.objects.create(name='ASDA', price_range=1.0, urls=['asda.com'], parent_company='Walmart Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.1, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 2.7, traceability_fti_rating = 3.5, \
                goy_link='https://directory.goodonyou.eco/brand/walmart', location='United States')

        Brand.objects.create(name='ASICS', price_range=2.0, urls=['asics.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 6.2, knowshow_fti_rating = 4.3, \
                spotlight_fti_rating = 3.4, traceability_fti_rating = 5.4, \
                goy_link='https://directory.goodonyou.eco/brand/asics', location='Australia')

        Brand.objects.create(name='ASOS', price_range=2.0, urls=['asos.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.3, governance_fti_rating = 4.6, knowshow_fti_rating = 4.0, \
                spotlight_fti_rating = 2.4, traceability_fti_rating = 6.2, \
                goy_link='https://directory.goodonyou.eco/brand/asos', location='United Kingdom')

        Brand.objects.create(name='Balenciaga', price_range=4.0, urls=['balenciaga.com'], parent_company='Kering',\
                planet_goy_rating = 8.0, animal_goy_rating = 6.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.5, governance_fti_rating = 8.5, knowshow_fti_rating = 4.5, \
                spotlight_fti_rating = 4.7, traceability_fti_rating = 1.1, \
                goy_link='https://directory.goodonyou.eco/brand/balenciaga', location='France')

        Brand.objects.create(name='Bally', price_range=4.0, urls=['bally.com'], parent_company='JAB Holding Company',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 4.2, governance_fti_rating = 3.1, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 1.7, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/bally', location='Switzerland')

        Brand.objects.create(name='Banana Republic', price_range=2.0, urls=['bananarepublic.gap.com'], parent_company='Gap Inc.',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.1, governance_fti_rating = 4.6, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 3.5, traceability_fti_rating = 4.5, \
                goy_link='https://directory.goodonyou.eco/brand/banana-republic', location='United States')

        Brand.objects.create(name='BCBGMAXAZRIA', price_range=3.0, urls=['bcbg.com'], parent_company='Centric Brands',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.5, governance_fti_rating = 0.0, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/bcbgmaxazria', location='United States')

        Brand.objects.create(name='Bershka', price_range=1.0, urls=['bershka.com'], parent_company='Inditex',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/bershka', location='Spain')

        Brand.objects.create(name='Billabong', price_range=2.0, urls=['billabong.com', 'billabong.ca'], parent_company='Boardriders',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/billabong', location='United States')

        Brand.objects.create(name='Bloomingdale\'s', price_range=3.0, urls=['bloomingdales.com'], parent_company='Macy\'s Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 4.8, governance_fti_rating = 1.5, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/bloomingdales', location='United States')

        Brand.objects.create(name='Bonprix', price_range=2.0, urls=['bonprix.com', 'venus.com'], parent_company='Otto Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 5.4, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 1.0, traceability_fti_rating = 4.1, \
                goy_link='https://directory.goodonyou.eco/brand/bonprix', location='United Kingdom')

        Brand.objects.create(name='boohoo', price_range=1.0, urls=['boohoo.com'], parent_company='Boohoo Group plc',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 5.2, governance_fti_rating = 4.6, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 1.8, \
                goy_link='https://directory.goodonyou.eco/brand/boohoo', location='United Kingdom')

        Brand.objects.create(name='Bosideng', price_range=3.0, urls=['bosideng.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 2.6, governance_fti_rating = 1.5, knowshow_fti_rating = 0.2, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/bosideng', location='China')

        Brand.objects.create(name='Bottega Veneta', price_range=4.0, urls=['bottegaveneta.com'], parent_company='Kering',\
                planet_goy_rating = 8.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.5, governance_fti_rating = 8.5, knowshow_fti_rating = 4.5, \
                spotlight_fti_rating = 4.6, traceability_fti_rating = 1.1, \
                goy_link='https://directory.goodonyou.eco/brand/bottega-veneta', location='Italy')

        Brand.objects.create(name='Brooks Sports', price_range=3.0, urls=['brooksrunning.com'], parent_company='Berkshire Hathaway',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.1, governance_fti_rating = 3.1, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 2.2, traceability_fti_rating = 3.1, \
                goy_link='https://directory.goodonyou.eco/brand/brooks', location='United States')

        Brand.objects.create(name='Brunello Cucinelli', price_range=3.0, urls=['brunellocucinelli.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 0.5, governance_fti_rating = 0.8, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/brunello-cucinelli', location='Italy')

        Brand.objects.create(name='Buckle', price_range=2.0, urls=['buckle.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 3.0, governance_fti_rating = 1.5, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/buckle', location='United States')

        Brand.objects.create(name='Burberry', price_range=4.0, urls=['burberry.com'], parent_company='',\
                planet_goy_rating = 8.0, animal_goy_rating = 4.0, people_goy_rating = 8.0,\
                policy_fti_rating = 8.6, governance_fti_rating = 6.2, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 4.0, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/burberry', location='United Kingdom')

        Brand.objects.create(name='Calvin Klein', price_range=3.0, urls=['calvinklein.com', 'calvinklein.ca'], parent_company='PVH',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 4.6, knowshow_fti_rating = 5.1, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 7.2, \
                goy_link='https://directory.goodonyou.eco/brand/calvin-klein', location='United States')

        Brand.objects.create(name='Calzedonia', price_range=2.0, urls=['calzedonia.com'], parent_company='Calzedonia Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.2, governance_fti_rating = 3.1, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/calzedonia', location='Italy')

        Brand.objects.create(name='Canada Goose', price_range=4.0, urls=['canadagoose.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.0, governance_fti_rating = 0.0, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.6, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/canada-goose', location='Canada')

        Brand.objects.create(name='Carhartt', price_range=3.0, urls=['carhartt.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.6, governance_fti_rating = 1.5, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 1.2, \
                goy_link='https://directory.goodonyou.eco/brand/carhartt', location='United States')

        Brand.objects.create(name='Carolina Herrera', price_range=4.0, urls=['carolinaherrera.com'], parent_company='Puig',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.3, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 1.4, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/carolina-herrera', location='United States')

        Brand.objects.create(name='CAROLL', price_range=2.0, urls=['caroll.com'], parent_company='Vivarte',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 4.7, governance_fti_rating = 0.8, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/caroll', location='France')

        Brand.objects.create(name='Carter\'s', price_range=1.0, urls=['carters.com'], parent_company='Carter\'s Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.0, governance_fti_rating = 1.5, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.4, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/carters', location='United States')

        Brand.objects.create(name='CELINE', price_range=4.0, urls=['celine.com'], parent_company='LVMH',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 7.7, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/celine', location='France')

        Brand.objects.create(name='Champion', price_range=2.0, urls=['champion.com'], parent_company='Hanesbrands Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 7.7, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 3.3, traceability_fti_rating = 3.9, \
                goy_link='https://directory.goodonyou.eco/brand/champion', location='United Kingdom')

        Brand.objects.create(name='Chanel', price_range=4.0, urls=['chanel.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.5, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/chanel', location='United Kingdom')

        Brand.objects.create(name='Chico\'s', price_range=2.0, urls=['chicos.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 3.9, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/chicos', location='United States')

        Brand.objects.create(name='Chloé', price_range=4.0, urls=['chloe.com'], parent_company='Richemont',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.5, governance_fti_rating = 6.2, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 1.3, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/chloe', location='France')

        Brand.objects.create(name='Claire\'s', price_range=1.0, urls=['claires.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 8.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.7, governance_fti_rating = 0.0, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/claires', location='United Kingdom')

        Brand.objects.create(name='Clarks', price_range=3.0, urls=['clarks.com', 'clarkscanada.com', 'clarksusa.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.7, governance_fti_rating = 3.8, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 5.5, \
                goy_link='https://directory.goodonyou.eco/brand/clarks', location='United Kingdom')

        Brand.objects.create(name='COACH', price_range=3.0, urls=['coach.com'], parent_company='Tapestry Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 2.0, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/coach', location='United States')

        Brand.objects.create(name='Cole Haan', price_range=3.0, urls=['colehaan.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 2.1, governance_fti_rating = 1.5, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/cole-haan', location='United States')

        Brand.objects.create(name='Columbia Sportswear', price_range=2.0, urls=['columbia.com', 'columbiasportswear.ca'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.5, governance_fti_rating = 4.6, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 1.6, traceability_fti_rating = 1.9, \
                goy_link='https://directory.goodonyou.eco/brand/columbia', location='United States')

        Brand.objects.create(name='Converse', price_range=2.0, urls=['converse.com', 'converse.ca'], parent_company='Nike Inc.',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 6.2, knowshow_fti_rating = 3.2, \
                spotlight_fti_rating = 4.8, traceability_fti_rating = 6.1, \
                goy_link='https://directory.goodonyou.eco/brand/converse', location='United States')

        Brand.objects.create(name='Cortefiel', price_range=2.0, urls=['cortefiel.com'], parent_company='Tendam',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 1.5, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 0.6, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/cortefiel', location='Spain')

        Brand.objects.create(name='Cotton On', price_range=1.0, urls=['cottonon.com'], parent_company='Cotton On Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.9, governance_fti_rating = 0.8, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 2.2, \
                goy_link='https://directory.goodonyou.eco/brand/cotton-on', location='Australia')

        Brand.objects.create(name='Decathlon', price_range=2.0, urls=['decathlon.com', 'decathlon.ca'], parent_company='Association Familiale Mulliez',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 1.5, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 2.5, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/decathlon', location='United States')

        Brand.objects.create(name='Deichmann', price_range=2.0, urls=['deichmann.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 1.8, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/deichmann', location='Germany')

        Brand.objects.create(name='Desigual', price_range=2.0, urls=['desigual.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.6, governance_fti_rating = 0.0, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.0, traceability_fti_rating = 2.3, \
                goy_link='https://directory.goodonyou.eco/brand/desigual', location='Spain')

        Brand.objects.create(name='Diesel', price_range=2.0, urls=['diesel.com'], parent_company='OTB Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/desigual', location='Spain')

        Brand.objects.create(name='Dillard\'s', price_range=2.0, urls=['dillards.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.9, governance_fti_rating = 1.5, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/dillards', location='United States')

        Brand.objects.create(name='Dior', price_range=4.0, urls=['dior.com'], parent_company='LVMH',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 7.7, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/dior', location='France')

        Brand.objects.create(name='DKNY', price_range=3.0, urls=['dkny.com'], parent_company='G-III Apparel Group',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.8, governance_fti_rating = 0.0, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/dkny', location='United States')

        Brand.objects.create(name='Dolce & Gabbana', price_range=4.0, urls=['dolcegabbana.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 1.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/dolce-and-gabbana', location='Italy')

        Brand.objects.create(name='Dr. Martens', price_range=3.0, urls=['drmartens.com'], parent_company='Permira',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.9, governance_fti_rating = 3.1, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 1.4, \
                goy_link='https://directory.goodonyou.eco/brand/dr-martens', location='United Kingdom')

        Brand.objects.create(name='Dressmann', price_range=2.0, urls=['dressmann.com'], parent_company='VARNER',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.2, governance_fti_rating = 6.2, knowshow_fti_rating = 4.9, \
                spotlight_fti_rating = 2.4, traceability_fti_rating = 5.5, \
                goy_link='https://directory.goodonyou.eco/brand/dressmann', location='Norway')

        Brand.objects.create(name='Eddie Bauer', price_range=3.0, urls=['eddiebauer.com'], parent_company='Golden Gate Capital',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.6, governance_fti_rating = 0.0, knowshow_fti_rating = 0.2, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/eddie-bauer', location='United States')

        Brand.objects.create(name='El Corte Inglés', price_range=3.0, urls=['elcorteingles.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.3, governance_fti_rating = 3.1, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 2.2, traceability_fti_rating = 1.6, \
                goy_link='https://directory.goodonyou.eco/brand/el-corte-ingles', location='Spain')

        Brand.objects.create(name='Elie Tahari', price_range=3.0, urls=['elietahari.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.0, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/elie-tahari', location='United States')

        Brand.objects.create(name='Ermenegildo Zegna', price_range=4.0, urls=['zegna.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.3, governance_fti_rating = 1.5, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 7.8, \
                goy_link='https://directory.goodonyou.eco/brand/ermenegildo-zegna', location='Italy')

        Brand.objects.create(name='Esprit', price_range=2.0, urls=['esprit.com', 'esprit-shop.ca'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.4, governance_fti_rating = 6.2, knowshow_fti_rating = 4.3, \
                spotlight_fti_rating = 3.3, traceability_fti_rating = 9.2, \
                goy_link='https://directory.goodonyou.eco/brand/esprit', location='Germany')

        Brand.objects.create(name='Express', price_range=2.0, urls=['express.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.3, governance_fti_rating = 1.5, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/express', location='United States')

        Brand.objects.create(name='Fashion Nova', price_range=2.0, urls=['fashionnova.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/fashion-nova', location='United States')

        Brand.objects.create(name='Fendi', price_range=4.0, urls=['fendi.com'], parent_company='LVMH',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 7.7, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.6, traceability_fti_rating = 6.6, \
                goy_link='https://directory.goodonyou.eco/brand/fendi', location='Italy')

        Brand.objects.create(name='Fila', price_range=2.0, urls=['fila.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 2.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.0, governance_fti_rating = 0.8, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/fila', location='Republic of Korea')

        Brand.objects.create(name='Fjällräven', price_range=2.0, urls=['fjallraven.com'], parent_company='Fenix Outdoor',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 6.2, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 2.4, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/fjallraven', location='Sweeden')

        Brand.objects.create(name='Foschini', price_range=2.0, urls=['foschini.com', 'foschini.co.za'], parent_company='TFG',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.2, governance_fti_rating = 3.1, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 1.4, \
                goy_link='https://directory.goodonyou.eco/brand/foschini', location='South Africa')

        Brand.objects.create(name='Fossil', price_range=2.0, urls=['fossil.com'], parent_company='Fossil Group Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.9, governance_fti_rating = 0.0, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/fossil', location='Australia')

        Brand.objects.create(name='Free people', price_range=2.0, urls=['freepeople.com'], parent_company='Urban Outfitters',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.0, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/free-people', location='United States')

        Brand.objects.create(name='Fruit of the Loom', price_range=2.0, urls=['fruit.com'], parent_company='Fruit of The Loom',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.1, knowshow_fti_rating = 2.8, \
                spotlight_fti_rating = 2.5, traceability_fti_rating = 3.5, \
                goy_link='https://directory.goodonyou.eco/brand/fruit-of-the-loom', location='United States')

        Brand.objects.create(name='Furla', price_range=3.0, urls=['furla.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 3.6, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/furla', location='Italy')

        Brand.objects.create(name='G-Star RAW', price_range=4.0, urls=['g-star.com'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.7, governance_fti_rating = 6.2, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 1.7, traceability_fti_rating = 5.8, \
                goy_link='https://directory.goodonyou.eco/brand/g-star-raw', location='Netherlands')

        Brand.objects.create(name='Gap', price_range=2.0, urls=['gap.com'], parent_company='Gap Inc.',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.1, governance_fti_rating = 4.6, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 3.5, traceability_fti_rating = 4.5, \
                goy_link='https://directory.goodonyou.eco/brand/gap', location='United States')

        Brand.objects.create(name='Gerry Weber', price_range=3.0, urls=['gerryweber.com'], parent_company='Gildan',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 1.6, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/gerry-weber', location='Germany')

        Brand.objects.create(name='Gucci', price_range=4.0, urls=['gucci.com'], parent_company='Kering',\
                planet_goy_rating = 8.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 8.5, knowshow_fti_rating = 4.5, \
                spotlight_fti_rating = 6.6, traceability_fti_rating = 3.1, \
                goy_link='https://directory.goodonyou.eco/brand/gucci', location='Italy')

        Brand.objects.create(name='GUESS', price_range=2.0, urls=['guess.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.4, governance_fti_rating = 2.3, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/guess', location='United States')

        Brand.objects.create(name='H&M', price_range=2.0, urls=['hm.com'], parent_company='H&M Group',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.7, governance_fti_rating = 8.5, knowshow_fti_rating = 5.1, \
                spotlight_fti_rating = 5.4, traceability_fti_rating = 8.1, \
                goy_link='https://directory.goodonyou.eco/brand/h-and-m', location='Sweden')

        Brand.objects.create(name='Hanes', price_range=2.0, urls=['hanes.com'], parent_company='Hanesbrands Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 7.7, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 3.3, traceability_fti_rating = 3.9, \
                goy_link='https://directory.goodonyou.eco/brand/hanes', location='United States')

        Brand.objects.create(name='Helly Hansen', price_range=3.0, urls=['hellyhansen.com'], parent_company='Canadian Tire Corporation',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.6, governance_fti_rating = 1.5, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 6.5, \
                goy_link='https://directory.goodonyou.eco/brand/helly-hansen', location='Norway')

        Brand.objects.create(name='Hermès', price_range=4.0, urls=['hermes.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.3, governance_fti_rating = 6.9, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 2.7, traceability_fti_rating = 2.3, \
                goy_link='https://directory.goodonyou.eco/brand/hermes', location='France')

        Brand.objects.create(name='Hollister Co.', price_range=2.0, urls=['hollisterco.com'], parent_company='Abercrombie and Fitch',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.7, governance_fti_rating = 3.1, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/hollister', location='United States')

        Brand.objects.create(name='Hugo Boss', price_range=3.0, urls=['hugoboss.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.7, governance_fti_rating = 8.5, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 1.9, traceability_fti_rating = 2.4, \
                goy_link='https://directory.goodonyou.eco/brand/hugo-boss', location='Germany')

        Brand.objects.create(name='Intimissimi', price_range=3.0, urls=['intimissimi.com'], parent_company='Calzedonia Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.2, governance_fti_rating = 3.1, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/intimissimi', location='Italy')

        Brand.objects.create(name='Jack & Jones', price_range=2.0, urls=['jackjones.com', 'jack-jones.ca'], parent_company='Bestseller A/S',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.4, traceability_fti_rating = 2.6, \
                goy_link='https://directory.goodonyou.eco/brand/jack-and-jones', location='Denmark')

        Brand.objects.create(name='Jessica Simpson', price_range=2.0, urls=['jessicasimpson.com'], parent_company='Sequentional Brands Group',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.0, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/jessica-simpson', location='United States')

        Brand.objects.create(name='Jil Sander', price_range=4.0, urls=['jilsander.com'], parent_company='Onward Holdings',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.5, governance_fti_rating = 0.0, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/jil-sander', location='Italy')

        Brand.objects.create(name='Jockey', price_range=2.0, urls=['jockey.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 6.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.4, governance_fti_rating = 0.0, knowshow_fti_rating = 0.2, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/jockey', location='United Kingdom')

        Brand.objects.create(name='John Lewis', price_range=3.0, urls=['johnlewis.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.1, governance_fti_rating = 1.5, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 2.5, traceability_fti_rating = 2.4, \
                goy_link='https://directory.goodonyou.eco/brand/john-lewis', location='United Kingdom')

        Brand.objects.create(name='JustFab', price_range=2.0, urls=['justfab.com', 'justfab.ca'], parent_company='TechStyle Fashion Group',\
                planet_goy_rating = 2.0, animal_goy_rating = 8.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.9, governance_fti_rating = 0.0, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/justfabb', location='United Kingdom')

        Brand.objects.create(name='K-Way', price_range=3.0, urls=['k-way.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.4, governance_fti_rating = 1.5, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/k-way', location='Italy')

        Brand.objects.create(name='Kate Spade', price_range=2.0, urls=['katespade.com'], parent_company='Tapestry Inc.',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 2.0, traceability_fti_rating = 0.9, \
                goy_link='https://directory.goodonyou.eco/brand/kate-spade', location='United States')

        Brand.objects.create(name='Kathmandu', price_range=2.0, urls=['kathmandu.com.au'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.2, governance_fti_rating = 1.5, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 2.7, \
                goy_link='https://directory.goodonyou.eco/brand/kathmandu', location='Australia')

        Brand.objects.create(name='Kiabi', price_range=1.0, urls=['kiabi.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.9, governance_fti_rating = 3.8, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 1.6, \
                goy_link='https://directory.goodonyou.eco/brand/kiabi', location='France')

        Brand.objects.create(name='Kmart Australia', price_range=1.0, urls=['kmart.com.au'], parent_company='Wesfarmers',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.6, governance_fti_rating = 6.2, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 4.5, traceability_fti_rating = 5.5, \
                goy_link='https://directory.goodonyou.eco/brand/kmart-australia', location='Australia')

        Brand.objects.create(name='La Redoute', price_range=2.0, urls=['laredoute.com'], parent_company='Galeries Lafayette Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.8, governance_fti_rating = 1.5, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/la-redoute', location='France')

        Brand.objects.create(name='Lacoste', price_range=2.0, urls=['lacoste.com'], parent_company='Maus Frères',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.0, governance_fti_rating = 3.1, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 1.3, traceability_fti_rating = 5.5, \
                goy_link='https://directory.goodonyou.eco/brand/lacoste', location='France')

        Brand.objects.create(name='Lands\' End', price_range=2.0, urls=['landsend.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 3.1, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/lands-end', location='United States')

        Brand.objects.create(name='Levi Strauss & Co', price_range=2.0, urls=['levi.com'], parent_company='',\
                planet_goy_rating = 8.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.3, governance_fti_rating = 6.2, knowshow_fti_rating = 2.8, \
                spotlight_fti_rating = 3.3, traceability_fti_rating = 4.3, \
                goy_link='https://directory.goodonyou.eco/brand/levis', location='United States')

        Brand.objects.create(name='Lindex', price_range=1.0, urls=['lindex.com'], parent_company='Stockmann Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.3, governance_fti_rating = 3.1, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 3.1, traceability_fti_rating = 8.2, \
                goy_link='https://directory.goodonyou.eco/brand/lindex', location='Sweden')

        Brand.objects.create(name='L.L. Bean', price_range=3.0, urls=['llbean.com', 'llbean.ca'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 2.0, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 1.9, \
                goy_link='https://directory.goodonyou.eco/brand/llbean', location='United States')

        Brand.objects.create(name='Longchamp', price_range=4.0, urls=['longchamp.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 1.2, governance_fti_rating = 1.5, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/longchamp', location='France')

        Brand.objects.create(name='Louis Vuitton', price_range=4.0, urls=['louisvuitton.com'], parent_company='LVMH',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 7.7, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/louis-vuitton', location='France')

        Brand.objects.create(name='Lululemon', price_range=3.0, urls=['lululemon.com', 'shop.lululemon.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.8, governance_fti_rating = 4.6, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 1.7, traceability_fti_rating = 5.9, \
                goy_link='https://directory.goodonyou.eco/brand/lululemon', location='Canada')

        Brand.objects.create(name='Macy\'s', price_range=3.0, urls=['macys.com'], parent_company="Macy's Inc.",\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 4.8, governance_fti_rating = 1.5, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/macys', location='United States')

        Brand.objects.create(name='Mammut', price_range=1.0, urls=['mammut.com'], parent_company='Conzzeta AG',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.2, governance_fti_rating = 1.5, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 2.7, traceability_fti_rating = 3.1, \
                goy_link='https://directory.goodonyou.eco/brand/mammut', location='Switzerland')

        Brand.objects.create(name='Mango', price_range=2.0, urls=['mango.com', 'shop.mango.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.5, governance_fti_rating = 1.5, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 2.2, traceability_fti_rating = 1.5, \
                goy_link='https://directory.goodonyou.eco/brand/mango', location='Spain')

        Brand.objects.create(name='Marc Jacobs', price_range=3.0, urls=['marcjacobs.com'], parent_company='LVMH',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 7.7, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 1.0, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/marc-jacobs', location='United States')

        Brand.objects.create(name='Marks & Spencer', price_range=1.0, urls=['marksandspencer.com'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.3, governance_fti_rating = 6.2, knowshow_fti_rating = 4.5, \
                spotlight_fti_rating = 2.9, traceability_fti_rating = 5.4, \
                goy_link='https://directory.goodonyou.eco/brand/marks-and-spencer', location='United Kingdom')

        Brand.objects.create(name='Marni', price_range=3.0, urls=['marni.com'], parent_company='OTB Group',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 2.8, governance_fti_rating = 0.0, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/marni', location='Italy')

        Brand.objects.create(name='Massimo Dutti', price_range=3.0, urls=['massimodutti.com'], parent_company='Inditex',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/massimo-dutti', location='Spain')

        Brand.objects.create(name='Matalan', price_range=1.0, urls=['matalan.com', 'matalan.co.uk'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.5, governance_fti_rating = 0.8, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 1.8, \
                goy_link='https://directory.goodonyou.eco/brand/matalan', location='United Kingdom')

        Brand.objects.create(name='Max Mara', price_range=3.0, urls=['maxmara.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.3, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/max-mara', location='Italy')

        Brand.objects.create(name='Merrell', price_range=2.0, urls=['merrell.com'], parent_company='Wolverine World Wide Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 3.9, governance_fti_rating = 0.0, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.4, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/merrell', location='United States')

        Brand.objects.create(name='Michael Kors', price_range=3.0, urls=['michaelkors.com', 'michaelkors.ca'], parent_company='Capri Holdings Limited',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 3.1, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/michael-kors', location='United States')

        Brand.objects.create(name='Miu Miu', price_range=4.0, urls=['miumiu.com'], parent_company='Prada Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.8, governance_fti_rating = 3.1, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 1.3, traceability_fti_rating = 1.5, \
                goy_link='https://directory.goodonyou.eco/brand/miu-miu', location='France')

        Brand.objects.create(name='Mizuno', price_range=4.0, urls=['mizunousa.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.4, governance_fti_rating = 1.5, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 2.3, \
                goy_link='https://directory.goodonyou.eco/brand/mizuno', location='Japan')

        Brand.objects.create(name='Moncler', price_range=4.0, urls=['moncler.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.9, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/moncler', location='Italy')

        Brand.objects.create(name='Muji', price_range=3.0, urls=['muji.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.5, governance_fti_rating = 3.1, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 1.4, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/muji', location='Japan')

        Brand.objects.create(name='New Balance', price_range=3.0, urls=['newbalance.com', 'newbalance.ca'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.1, governance_fti_rating = 5.4, knowshow_fti_rating = 3.8, \
                spotlight_fti_rating = 2.3, traceability_fti_rating = 4.7, \
                goy_link='https://directory.goodonyou.eco/brand/new-balance', location='United States')

        Brand.objects.create(name='New Look', price_range=2.0, urls=['newlook.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.8, governance_fti_rating = 4.6, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 4.1, \
                goy_link='https://directory.goodonyou.eco/brand/new-look', location='United Kingdom')

        Brand.objects.create(name='New Yorker', price_range=1.0, urls=['newyorker.de'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.3, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/new-yorker', location='Germany')

        Brand.objects.create(name='Next', price_range=2.0, urls=['nextdirect.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 2.3, knowshow_fti_rating = 3.6, \
                spotlight_fti_rating = 2.8, traceability_fti_rating = 3.6, \
                goy_link='https://directory.goodonyou.eco/brand/next', location='United Kingdom')

        Brand.objects.create(name='Nike', price_range=3.0, urls=['nike.com'], parent_company='Nike, Inc.',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 6.2, knowshow_fti_rating = 3.2, \
                spotlight_fti_rating = 4.8, traceability_fti_rating = 6.1, \
                goy_link='https://directory.goodonyou.eco/brand/nike', location='United States')

        Brand.objects.create(name='Nordstrom', price_range=3.0, urls=['nordstrom.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.1, knowshow_fti_rating = 2.3, \
                spotlight_fti_rating = 2.3, traceability_fti_rating = 0.2, \
                goy_link='https://directory.goodonyou.eco/brand/nordstrom', location='United States')

        Brand.objects.create(name='Old Navy', price_range=1.0, urls=['oldnavy.com', 'oldnavy.gap.com'], parent_company='Gap Inc.',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.1, governance_fti_rating = 4.6, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 3.5, traceability_fti_rating = 4.5, \
                goy_link='https://directory.goodonyou.eco/brand/old-navy', location='United States')

        Brand.objects.create(name='OTTO', price_range=2.0, urls=['ottostore.com'], parent_company='Otto Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.6, governance_fti_rating = 4.6, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 1.4, \
                goy_link='https://directory.goodonyou.eco/brand/otto', location='Germany')

        Brand.objects.create(name='OVS', price_range=2.0, urls=['ovsfashion.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 7.8, governance_fti_rating = 7.7, knowshow_fti_rating = 5.5, \
                spotlight_fti_rating = 7.2, traceability_fti_rating = 9.3, \
                goy_link='https://directory.goodonyou.eco/brand/ovs', location='Italy')

        Brand.objects.create(name='Patagonia', price_range=2.0, urls=['patagonia.com', 'patagonia.ca'], parent_company='',\
                planet_goy_rating = 8.0, animal_goy_rating = 8.0, people_goy_rating = 8.0,\
                policy_fti_rating = 7.8, governance_fti_rating = 5.4, knowshow_fti_rating = 4.7, \
                spotlight_fti_rating = 4.1, traceability_fti_rating = 6.8, \
                goy_link='https://directory.goodonyou.eco/brand/patagonia', location='United States')

        Brand.objects.create(name='Pepe Jeans', price_range=2.0, urls=['pepejeans.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/pepe-jeans', location='Spain')

        Brand.objects.create(name='Pimkie', price_range=2.0, urls=['pimkie.com', 'pimkie.de', 'pimkie.fr'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.5, governance_fti_rating = 5.4, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 2.3, traceability_fti_rating = 2.4, \
                goy_link='https://directory.goodonyou.eco/brand/pimkie', location='France')

        Brand.objects.create(name='Prada', price_range=4.0, urls=['prada.com'], parent_company='Prada Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 2.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.8, governance_fti_rating = 3.1, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 1.3, traceability_fti_rating = 1.5, \
                goy_link='https://directory.goodonyou.eco/brand/prada', location='Italy')

        Brand.objects.create(name='PrettyLittleThing', price_range=2.0, urls=['prettylittlething.com'], parent_company='Boohoo Group plc',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 5.2, governance_fti_rating = 4.6, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 1.8, \
                goy_link='https://directory.goodonyou.eco/brand/prettylittlething', location='United Kingdom')

        Brand.objects.create(name='Primark', price_range=1.0, urls=['primark.com'], parent_company='Associated British Foods plc',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.5, governance_fti_rating = 3.8, knowshow_fti_rating = 4.3, \
                spotlight_fti_rating = 3.0, traceability_fti_rating = 2.3, \
                goy_link='https://directory.goodonyou.eco/brand/primark', location='United States')

        Brand.objects.create(name='Pull&Bear', price_range=1.0, urls=['pullandbear.com'], parent_company='Inditex',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 4.3, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/pull-and-bear', location='Spain')

        Brand.objects.create(name='Puma', price_range=2.0, urls=['puma.com'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.4, governance_fti_rating = 8.5, knowshow_fti_rating = 5.1, \
                spotlight_fti_rating = 3.7, traceability_fti_rating = 4.1, \
                goy_link='https://directory.goodonyou.eco/brand/puma', location='Germany')

        Brand.objects.create(name='Quiksilver', price_range=2.0, urls=['quiksilver.com', 'quiksilver-shop.ca'], parent_company='Boardriders',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/quiksilver', location='United States')

        Brand.objects.create(name='Ralph Lauren', price_range=4.0, urls=['ralphlauren.com'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.1, governance_fti_rating = 4.6, knowshow_fti_rating = 2.8, \
                spotlight_fti_rating = 3.4, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/ralph-lauren', location='United States')

        Brand.objects.create(name='Reebok', price_range=3.0, urls=['reebook.com', 'reebok.ca'], parent_company='Adidas AG',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.1, governance_fti_rating = 6.2, knowshow_fti_rating = 4.9, \
                spotlight_fti_rating = 3.9, traceability_fti_rating = 5.8, \
                goy_link='https://directory.goodonyou.eco/brand/reebok', location='United States')

        Brand.objects.create(name='REI', price_range=2.0, urls=['rei.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.0, governance_fti_rating = 2.3, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 1.6, traceability_fti_rating = 1.5, \
                goy_link='https://directory.goodonyou.eco/brand/rei', location='United States')

        Brand.objects.create(name='Reserved', price_range=2.0, urls=['reserved.com'], parent_company='LPP',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.2, governance_fti_rating = 2.3, knowshow_fti_rating = 0.6, \
                spotlight_fti_rating = 1.7, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/reserved', location='Poland')

        Brand.objects.create(name='REVOLVE', price_range=3.0, urls=['revolve.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 3.1, knowshow_fti_rating = 0.2, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/revolve', location='United States')

        Brand.objects.create(name='River Island', price_range=2.0, urls=['riverisland.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.8, knowshow_fti_rating = 1.9, \
                spotlight_fti_rating = 0.1, traceability_fti_rating = 2.6, \
                goy_link='https://directory.goodonyou.eco/brand/river-island', location='United Kingdom')

        Brand.objects.create(name='Roxy', price_range=2.0, urls=['roxy.com, roxy.ca'], parent_company='Boardriders',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/roxy', location='United States')

        Brand.objects.create(name='Russell Athletic', price_range=1.0, urls=['russellathletic.com'], parent_company='Fruit of the Loom',\
                planet_goy_rating = 4.0, animal_goy_rating = 8.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.1, knowshow_fti_rating = 2.8, \
                spotlight_fti_rating = 2.5, traceability_fti_rating = 3.5, \
                goy_link='https://directory.goodonyou.eco/brand/russell-athletic', location='United States')

        Brand.objects.create(name='s.Oliver', price_range=2.0, urls=['soliver.com', 'soliver.eu'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.5, governance_fti_rating = 0.8, knowshow_fti_rating = 0.4, \
                spotlight_fti_rating = 0.6, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/soliver', location='Germany')

        Brand.objects.create(name='Saint Laurent', price_range=4.0, urls=['ysl.com'], parent_company='Kering',\
                planet_goy_rating = 8.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.5, governance_fti_rating = 8.5, knowshow_fti_rating = 4.5, \
                spotlight_fti_rating = 4.7, traceability_fti_rating = 1.1, \
                goy_link='https://directory.goodonyou.eco/brand/saint-laurent', location='France')

        Brand.objects.create(name='Salvatore Ferragamo', price_range=4.0, urls=['ferragamo.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.7, governance_fti_rating = 6.2, knowshow_fti_rating = 2.6, \
                spotlight_fti_rating = 2.4, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/salvatore-ferragamo', location='Italy')

        Brand.objects.create(name='Sandro', price_range=4.0, urls=['sandro-paris.com'], parent_company='SMCP',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 3.9, governance_fti_rating = 0.8, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 0.5, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/sandro', location='France')

        Brand.objects.create(name='SHEIN', price_range=3.0, urls=['shein.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 4.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.8, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/shein', location='China')

        Brand.objects.create(name='Stradivarius', price_range=1.0, urls=['stradivarius.com'], parent_company='Inditex',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/stradivarius', location='Spain')

        Brand.objects.create(name='Superdry', price_range=3.0, urls=['superdry.com', 'superdrystore.ca'], parent_company='',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.0, governance_fti_rating = 6.2, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 4.1, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/superdry', location='United Kingdom')

        Brand.objects.create(name='Takko', price_range=0, urls=['takko.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 8.0, people_goy_rating = 6.0,\
                policy_fti_rating = 3.4, governance_fti_rating = 0.0, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 0.5, \
                goy_link='https://directory.goodonyou.eco/brand/takko', location='')

        Brand.objects.create(name='Target Australia', price_range=1.0, urls=['target.com.au'], parent_company='Wesfarmers',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.6, governance_fti_rating = 6.2, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 4.5, traceability_fti_rating = 5.5, \
                goy_link='https://directory.goodonyou.eco/brand/target-australia', location='United States')

        Brand.objects.create(name='Ted Baker', price_range=2.0, urls=['tedbaker.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.5, governance_fti_rating = 1.5, knowshow_fti_rating = 0.9, \
                spotlight_fti_rating = 1.2, traceability_fti_rating = 2.6, \
                goy_link='https://directory.goodonyou.eco/brand/ted-baker', location='United Kingdom')

        Brand.objects.create(name='The North Face', price_range=3.0, urls=['thenorthface.com'], parent_company='VF Corporation',\
                planet_goy_rating = 6.0, animal_goy_rating = 8.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 6.2, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 4.7, traceability_fti_rating = 8.4, \
                goy_link='https://directory.goodonyou.eco/brand/the-north-face', location='United States')

        Brand.objects.create(name='Timberland', price_range=2.0, urls=['timberland.com', 'timberland.ca'], parent_company='VF Corporation',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 6.2, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 4.7, traceability_fti_rating = 8.4, \
                goy_link='https://directory.goodonyou.eco/brand/timberland', location='United States')

        Brand.objects.create(name='Tod\'s', price_range=3.0, urls=['tods.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.3, governance_fti_rating = 3.8, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.3, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/tods', location='Italy')

        Brand.objects.create(name='Tom Ford', price_range=4.0, urls=['tomford.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.2, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/tom-ford', location='United States')

        Brand.objects.create(name='Tom Tailor', price_range=2.0, urls=['tom-tailor.com', 'tom-tailor.eu'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.6, governance_fti_rating = 3.1, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 6.9, \
                goy_link='https://directory.goodonyou.eco/brand/tom-tailor', location='Germany')

        Brand.objects.create(name='Tommy Hilfiger', price_range=2.0, urls=['global.tommy.com', 'usa.tommy.com'], parent_company='PVH',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 4.6, knowshow_fti_rating = 5.1, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 7.2, \
                goy_link='https://directory.goodonyou.eco/brand/tommy-hilfiger', location='United States')

        Brand.objects.create(name='Tory Burch', price_range=3.0, urls=['toryburch.com'], parent_company='',\
                planet_goy_rating = 2.0, animal_goy_rating = 0.0, people_goy_rating = 2.0,\
                policy_fti_rating = 0.3, governance_fti_rating = 0.0, knowshow_fti_rating = 0.0, \
                spotlight_fti_rating = 0.0, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/tory-burch', location='United States')

        Brand.objects.create(name='Under Armour', price_range=2.0, urls=['underarmour.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.1, governance_fti_rating = 2.3, knowshow_fti_rating = 2.1, \
                spotlight_fti_rating = 0.7, traceability_fti_rating = 2.4, \
                goy_link='https://directory.goodonyou.eco/brand/under-armour', location='United States')

        Brand.objects.create(name='Uniqlo', price_range=1.0, urls=['uniqlo.com'], parent_company='Fast Retailing',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.6, governance_fti_rating = 4.6, knowshow_fti_rating = 4.3, \
                spotlight_fti_rating = 3.3, traceability_fti_rating = 3.2, \
                goy_link='https://directory.goodonyou.eco/brand/uniqlo', location='Japan')

        Brand.objects.create(name='United Colors of Benetton', price_range=2.0, urls=['world.benetton.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 4.6, knowshow_fti_rating = 4.0, \
                spotlight_fti_rating = 3.7, traceability_fti_rating = 8.5, \
                goy_link='https://directory.goodonyou.eco/brand/united-colors-of-benetton', location='Italy')

        Brand.objects.create(name='Urban Outfitters', price_range=3.0, urls=['urbanoutfitters.com'], parent_company='Urban Outfitters',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 4.0, governance_fti_rating = 3.1, knowshow_fti_rating = 1.5, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/urban-outfitters', location='United States')

        Brand.objects.create(name='Valentino', price_range=4.0, urls=['valentino.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 3.1, governance_fti_rating = 1.5, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 0.2, traceability_fti_rating = 0.0, \
                goy_link='https://directory.goodonyou.eco/brand/valentino', location='Italy')

        Brand.objects.create(name='Van Heusen', price_range=2.0, urls=['vanheusen.com'], parent_company='PVH',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 6.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 4.6, knowshow_fti_rating = 5.1, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 7.2, \
                goy_link='https://directory.goodonyou.eco/brand/van-heusen', location='United States')

        Brand.objects.create(name='Vans', price_range=2.0, urls=['vans.com'], parent_company='VF Corporation',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 9.2, governance_fti_rating = 6.2, knowshow_fti_rating = 5.3, \
                spotlight_fti_rating = 4.5, traceability_fti_rating = 8.4, \
                goy_link='https://directory.goodonyou.eco/brand/vans', location='United States')

        Brand.objects.create(name='Vero Moda', price_range=2.0, urls=['veromoda.com'], parent_company='Bestseller A/S',\
                planet_goy_rating = 6.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 6.4, governance_fti_rating = 3.1, knowshow_fti_rating = 1.3, \
                spotlight_fti_rating = 1.6, traceability_fti_rating = 2.6, \
                goy_link='https://directory.goodonyou.eco/brand/vero-moda', location='Denmark')

        Brand.objects.create(name='Versace', price_range=4.0, urls=['versace.com'], parent_company='Capri Holdings',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 5.8, governance_fti_rating = 3.1, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 0.8, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/versace', location='Italy')

        Brand.objects.create(name='Very', price_range=2.0, urls=['very.co.uk'], parent_company='The Very Group',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 1.5, knowshow_fti_rating = 1.7, \
                spotlight_fti_rating = 1.1, traceability_fti_rating = 0.2, \
                goy_link='https://directory.goodonyou.eco/brand/very', location='United Kingdom')

        Brand.objects.create(name='Walmart', price_range=1.0, urls=['walmart.com'], parent_company='Walmart Inc.',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.7, governance_fti_rating = 6.2, knowshow_fti_rating = 3.2, \
                spotlight_fti_rating = 1.8, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/walmart', location='United States')

        Brand.objects.create(name='Wrangler', price_range=2.0, urls=['wrangler.com'], parent_company='Kontoor',\
                planet_goy_rating = 6.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.4, governance_fti_rating = 2.3, knowshow_fti_rating = 1.1, \
                spotlight_fti_rating = 2.3, traceability_fti_rating = 4.6, \
                goy_link='https://directory.goodonyou.eco/brand/wrangler', location='United States')

        Brand.objects.create(name='Zara', price_range=1.0, urls=['zara.com'], parent_company='Inditex',\
                planet_goy_rating = 4.0, animal_goy_rating = 4.0, people_goy_rating = 4.0,\
                policy_fti_rating = 8.9, governance_fti_rating = 6.2, knowshow_fti_rating = 3.4, \
                spotlight_fti_rating = 4.2, traceability_fti_rating = 0.1, \
                goy_link='https://directory.goodonyou.eco/brand/zara', location='Spain')

        Brand.objects.create(name='Zeeman', price_range=1.0, urls=['zeeman.com'], parent_company='',\
                planet_goy_rating = 4.0, animal_goy_rating = 6.0, people_goy_rating = 4.0,\
                policy_fti_rating = 7.0, governance_fti_rating = 5.4, knowshow_fti_rating = 3.0, \
                spotlight_fti_rating = 2.3, traceability_fti_rating = 4.2, \
                goy_link='https://directory.goodonyou.eco/brand/zeeman', location='Netherlands')
