import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    """this command forces django app to wait for db initialization"""

    def handle(self, *args, **options):
        """command execution handler"""
        self.stdout.write('waiting for database....')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('db unavailable, will '
                                  'wait another second.... ')
                time.sleep(1)

        self.stdout.write('Db connection acquired...')
