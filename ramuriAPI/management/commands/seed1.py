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