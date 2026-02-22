"""
Configuration Loader with Mocked File I/O:

    Define a class ConfigLoader with an __init__ method.

    Add a method load_config(self, filepath) that conceptually reads a configuration from a file. In a real scenario, this would use open() and json.load() or similar. For this exercise, assume it reads a dictionary. If the file is config.json, it returns {"debug": True, "log_level": "INFO"}. If it's empty.json, it returns {}. If any other file, it should raise a FileNotFoundError.

    Write a function get_debug_status(config_loader, filename) that takes a ConfigLoader instance and a filename, calls config_loader.load_config(filename), and returns the value of the "debug" key, or False if not found or an error occurs.

    Write unit tests for get_debug_status. Use unittest.mock.Mock to mock the ConfigLoader object. Configure the mock load_config method to return different dictionaries or raise FileNotFoundError to test all scenarios.
"""

import unittest
from unittest.mock import Mock


class ConfigLoader:
    def __init__(self):
        """
        Initialize ConfigLoader object
        """
        pass

    def load_config(self, filepath):
        """
        Read a configuration from a file
        """
        if filepath == "config.json":
            return {"debug": True, "log_level": "INFO"}
        elif filepath == "empty.json":
            return {}
        else:
            raise FileNotFoundError


def get_debug_status(config_loader, filename):
    """
    calls config_loader.load_config(filename) and return the value of the debug key, or false if not
    found or an error
    """
    try:
        config = config_loader.load_config(filename)
        # Safely get "debug" value, defaulting to False if not present
        return config.get("debug", False)
    except FileNotFoundError:
        return False
    except Exception:
        return False


reloader = ConfigLoader()
# print(get_debug_status(reloader, "empty.json"))
# print(get_debug_status(reloader, "config.json"))
# print(get_debug_status(reloader, "test.json"))


class TestConfigLoader(unittest.TestCase):
    """
    Test cases for ConfigLoader class
    """

    def test_get_debug_status_config_found(self):
        """
        Test get_debug_status function works successfully
        """
        mock_config_loader = Mock()
        mock_config_loader.load_config.return_value = {
            "debug": True,
            "log_level": "INFO",
        }

        status = get_debug_status(mock_config_loader, "config.json")

        self.assertTrue(status)
        mock_config_loader.load_config.assert_called_once_with("config.json")

    def test_get_debug_status_empty_config(self):
        """
        test get_debug_status function when and empty file is passed in the argument
        """
        mock_config_loader = Mock()
        mock_config_loader.load_config.return_value = {}

        status = get_debug_status(mock_config_loader, "empty.json")

        self.assertFalse(status)
        mock_config_loader.load_config.assert_called_once_with("empty.json")

    def test_get_debug_status_debug_key_missing(self):
        """
        test get_debug_status function when debug key is missing
        """
        mock_config_loader = Mock()
        mock_config_loader.load_config.return_value = {
            "no_debug": True,
            "log_level": "INFO",
        }

        status = get_debug_status(mock_config_loader, "config.json")

        self.assertFalse(status)
        mock_config_loader.load_config.assert_called_once_with("config.json")

    def test_get_debug_status_file_not_found(self):
        """
        test get_debug_status function when file not found
        """
        mock_config_loader = Mock()

        # This makes the mock method raise the error when called.
        mock_config_loader.load_config.side_effect = FileNotFoundError

        status = get_debug_status(mock_config_loader, "nonexistent.json")

        self.assertFalse(status)
        mock_config_loader.load_config.assert_called_once_with("nonexistent.json")


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
