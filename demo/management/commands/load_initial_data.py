import os, shutil

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, **options):
        fixtures_dir = os.path.join(settings.PROJECT_ROOT, 'demo', 'fixtures')
        fixture_file = os.path.join(fixtures_dir, 'demo.json')

        call_command('loaddata', fixture_file, verbosity=0)

