import requests


class APIManager:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_server_health(self, endpoint="/health"):
        """
        Fetches the health status from an API endpoint
        """
        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()  # Raise an exception for HTTP Errors
            return response.json().get("status", "UNKNOWN")
        except requests.exceptions.RequestException as e:
            print(f"API request failed {e}")
            return "ERROR"


import unittest
from unittest.mock import patch, Mock


class TestAPIManager(unittest.TestCase):
    # Patch requests. get which APIManager internally uses
    @patch("requests.get")
    def test_get_server_health_success(self, mock_get):
        # Configure the mock requests.get to return a mock response object
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "healthy"}
        mock_response.raise_for_status.return_value = None  # No exception raised
        mock_get.return_value = mock_response

        # Instantiate APIManager and call the method under test
        api_manager = APIManager("http://test.api.com")
        status = api_manager.get_server_health()

        # Assertions
        self.assertEqual(status, "healthy")
        mock_get.assert_called_once_with("http://test.api.com/health")
        mock_response.json.assert_called_once()

    @patch("requests.get")
    def test_get_server_health_api_error(self, mock_get):
        # Configure mock requests.get to raise an HTTPError
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "500 Server Error"
        )
        mock_get.return_value = mock_response

        api_manager = APIManager("http://test.api.com")
        status = api_manager.get_server_health()

        self.assertEqual(status, "ERROR")
        mock_get.assert_called_once_with("http://test.api.com/health")
        # Ensure json() was not called if an error occurred before it
        mock_response.json.assert_not_called()


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
