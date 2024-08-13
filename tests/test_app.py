import unittest
from urllib import request

from leave_a_note import app


class TestApp(unittest.TestCase):
    def setUp(self):
        # tests run on localhost server
        # which is set up from makefile
        self.app_root = "http://localhost:8080"

    def test_home_page_response(self):
        """Testing webpage response code"""
        print("Testing page loads with correct status code")

        response = request.urlopen(self.app_root)
        self.assertEqual(response.status, 200)
