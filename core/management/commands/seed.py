from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import FieldUpdate

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        FieldUpdate.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        u1 = User.objects.create_user(username='john', first_name='John', last_name='Doe', email='john@farm.com', password='pass1234')
        u2 = User.objects.create_user(username='sarah', first_name='Sarah', last_name='Smith', email='sarah@farm.com', password='pass1234')
        u3 = User.objects.create_user(username='mike', first_name='Mike', last_name='Jones', email='mike@farm.com', password='pass1234')

        FieldUpdate.objects.create(author=u1, title='Locust Swarm Spotted', message='Large swarm moving towards corn fields in the North District.', category='pest_alert')
        FieldUpdate.objects.create(author=u1, title='Wheat Looking Good', message='The new fertilizer mix seems to be working wonders this season.', category='crop_condition')
        FieldUpdate.objects.create(author=u2, title='Heavy Rain Expected', message='Storm system moving in from the east, expect 3 days of heavy rain.', category='weather')
        FieldUpdate.objects.create(author=u2, title='NPK Ratio Tip', message='Increase potassium levels before the dry season for better root development.', category='fertilizer')
        FieldUpdate.objects.create(author=u3, title='Aphids on Tomatoes', message='Spotted aphid colonies on tomato plants in sector B. Spray immediately.', category='pest_alert')
        FieldUpdate.objects.create(author=u3, title='General Harvest Insight', message='Early morning harvesting reduces moisture loss significantly.', category='general')

        self.stdout.write(self.style.SUCCESS('Seed data created successfully!'))