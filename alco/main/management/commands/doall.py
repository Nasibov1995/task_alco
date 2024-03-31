
from django.core.management import BaseCommand,call_command


class Command(BaseCommand):
    help = ''
    
    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")