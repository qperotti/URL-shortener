from django.core.management.base import BaseCommand, CommandError

from shortener.models import QprttURL

class Command(BaseCommand):
    help = 'Refreshes all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int) # '--items' to make it optional

    def handle(self, *args, **options):
        QprttURL.objects.refresh_shortcodes(items=options['items'])

