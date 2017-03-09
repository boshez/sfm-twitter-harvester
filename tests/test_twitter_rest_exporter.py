from __future__ import absolute_import
import tests
from tests.tweets import tweet2
from twitter_rest_exporter import TwitterRestStatusTable
from datetime import datetime


class TestTwitterStatusTable(tests.TestCase):
    def test_row(self):
        table = TwitterRestStatusTable(None, None, None, None, None, None)
        row = table._row(tweet2)
        self.assertIsInstance(row[0], datetime)
        self.assertEqual("660065173563158529", row[1])
        self.assertEqual("justin_littman", row[2])
        self.assertEqual("", row[3])
        self.assertEqual(52, row[4])
        self.assertEqual(50, row[5])
        self.assertEqual(9, row[6])
        self.assertEqual(10, row[7])
        self.assertEqual("http://twitter.com/justin_littman/status/660065173563158529", row[11])
        self.assertEqual("My new blog post on techniques for harvesting social media to WARCs: https://t.co/OHZki6pXEe",
                         row[12])
        self.assertEqual("No", row[13])
        self.assertEqual("No", row[14])
        self.assertEqual("", row[15])
        self.assertEqual("https://t.co/OHZki6pXEe", row[16])
        self.assertEqual("http://bit.ly/1ipwd0B", row[17])
        self.assertEqual("", row[18])
        self.assertEqual("", row[19])
        self.assertEqual("", row[20])
