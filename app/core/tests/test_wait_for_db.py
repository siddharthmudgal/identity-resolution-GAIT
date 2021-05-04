from unittest import TestCase
from unittest.mock import patch

from django.core.management import call_command


class TestCommand(TestCase):

    def test_wait_for_db(self):
        """test waiting for database when db is available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)
