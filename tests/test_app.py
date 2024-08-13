import unittest

from webtest import TestApp

from leave_a_note import app


class MyTestApp(unittest.TestCase):
    def setUp(self):
        # tests run on localhost server
        # which is set up from makefile
        self.test_server = TestApp(app.app)

    def test_home_page_response(self):
        """Testing webpage response code"""
        print("Testing page loads with correct status code")

        response = self.test_server.get("/")

        assert response.status_code == 200
        assert response.status == "200 OK"

        response.mustcontain("<h1>Leave a note</h1>")
        response.mustcontain("<html")

    def test_static_files(self):
        """Test static files exist and can be found"""
        response = self.test_server.get("/static/styles.css")

        assert response.status_code == 200
        assert response.status == "200 OK"

        response = self.test_server.get("/static/scripts.js")

        assert response.status_code == 200
        assert response.status == "200 OK"
