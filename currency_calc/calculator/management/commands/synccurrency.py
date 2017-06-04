from django.core.management.base import BaseCommand, CommandError
from calculator.models import Currency
from calculator.services import createCurrencyInstances

class Command(BaseCommand):
    help = 'Syncronizes all exchange rates from bnb'

    def handle(self, *args, **options):
        return createCurrencyInstances()
