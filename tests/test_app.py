import pandas as pd
import pytest
from flask import Flask
from flask_testing import TestCase

from epl_pool.app import app, owner_team_data


class FlaskTestCase(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        return app

    def setUp(self):
        # Setup any state specific to the test execution
        pass

    def tearDown(self):
        # Clean up any necessary state after test execution
        pass

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"EPL Pool", response.data)

    def test_html_table(self):
        with app.test_client() as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            assert b'<table class="table">' in response.data

    def test_owner_team_data(self):
        assert "Arsenal" in owner_team_data["Squad"]
        assert "Casey" in owner_team_data["Owner"]


if __name__ == "__main__":
    pytest.main()
