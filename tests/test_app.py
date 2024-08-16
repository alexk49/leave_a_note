import os
import shutil
import sqlite3
import unittest

from webtest import TestApp

from leave_a_note import app


class MyTestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Run at start of all tests
        tests run on localhost server
        which is set up from makefile
        """
        cls.test_server = TestApp(app.app)
        cls.test_db_dir_path = "test_data"
        cls.test_db_name = "test_notes.db"
        cls.test_db_path = os.path.join(cls.test_db_dir_path, cls.test_db_name)

        cls.check_test_database_exists()

    @classmethod
    def tearDownClass(cls):
        """Run at end of all tests"""
        # delete test dir
        shutil.rmtree(cls.test_db_dir_path)

    @classmethod
    def check_test_database_exists(cls):
        """Used as utility method to create new test db
        but also tests the app.check_database_exists function"""
        assert not (os.path.exists(cls.test_db_path))

        app.check_database_exists(cls.test_db_dir_path, cls.test_db_path)

        assert os.path.exists(cls.test_db_path)

    def test_database_schema(self):
        """In order to execute commands you have to create a connection
        and then a database cursor"""
        connection = sqlite3.connect(self.test_db_path)
        cursor = connection.cursor()
        # query the schema for all tables
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
        schemas = cursor.fetchall()

        connection.close()

        # this will include notes db schema
        # and sqlite3_sequence table schema
        # which is made when using autoincrement
        self.assertEqual(len(schemas), 2)

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
