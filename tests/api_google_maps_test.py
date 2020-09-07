"""
   This module checks the connection to Google maps.

    Classes:
    TestGoogleApi

    Exceptions:
    NIL

    Functions:
    NIL
    """

import pytest
from app.controller.api_folder.api_google_maps import GoogleApi
from tests.conftest import TestWikipediaRequest


class TestGoogleApi(GoogleApi, TestWikipediaRequest):
    """
        Basic development. As for now only the connection is tested (code 200)
        """

    def test_connection_static_ok(self):
        response = self._response_google_static(self.mock_location_name)
        assert response.status_code == 200

    def test_connection_dynamic_ok(self):
        response = self._response_google_dynamic(self.mock_location_name)
        assert response.status_code == 200
