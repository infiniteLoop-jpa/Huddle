from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
import requests

class ExternalApiViewTest(TestCase):
    def setUp(self):
        # Create a mock response for the external API request
        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {'title': 'Test Post'}

    @patch('requests.get')
    def test_external_api_view_success(self, mock_get):
        # Configure the mock to return the mock response
        mock_get.return_value = self.mock_response

        # Issue a GET request to the 'external_api' URL
        response = self.client.get(reverse('external_api'))

        # Check if the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected JSON data
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'title': 'Test Post'})

    @patch('requests.get')
    def test_external_api_view_failure(self, mock_get):
        # Configure the mock to raise an exception to simulate a request failure
        mock_get.side_effect = requests.exceptions.RequestException("Request failed")

        # Issue a GET request to the 'external_api' URL
        response = self.client.get(reverse('external_api'))

        # Check if the response has a status code of 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response contains an error message
        self.assertContains(response, "An error occurred while fetching data from the external API")

    @patch('requests.get')
    def test_external_api_view_timeout(self, mock_get):
        # Configure the mock to raise a timeout exception to simulate a request timeout
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        # Issue a GET request to the 'external_api' URL
        response = self.client.get(reverse('external_api'))

        # Check if the response has a status code of 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response contains a timeout error message
        self.assertContains(response, "The request to the external API timed out")

    @patch('requests.get')
    def test_external_api_view_connection_error(self, mock_get):
        # Configure the mock to raise a connection error to simulate a connection issue
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")

        # Issue a GET request to the 'external_api' URL
        response = self.client.get(reverse('external_api'))

        # Check if the response has a status code of 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response contains a connection error message
        self.assertContains(response, "A connection error occurred while fetching data from the external API")
