import unittest

import requests

from leave_a_note import app


class TestApp(unittest.TestCase):
    def setUp(self):
        # tests run on localhost server
        # which is set up from makefile
        self.app_url = "http://localhost:8080/"

    def test_home_page_response(self):
        """Testing webpage response code"""
        print(f"Testing page loads with correct status code")
        response = requests.get(self.app_url)
        self.assertEqual(response.status_code, 200)
