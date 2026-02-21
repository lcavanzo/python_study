"""
Configuration Loader with Mocked File I/O:

    Define a class ConfigLoader with an __init__ method.

    Add a method load_config(self, filepath) that conceptually reads a configuration from a file. In a real scenario, this would use open() and json.load() or similar. For this exercise, assume it reads a dictionary. If the file is config.json, it returns {"debug": True, "log_level": "INFO"}. If it's empty.json, it returns {}. If any other file, it should raise a FileNotFoundError.

    Write a function get_debug_status(config_loader, filename) that takes a ConfigLoader instance and a filename, calls config_loader.load_config(filename), and returns the value of the "debug" key, or False if not found or an error occurs.

    Write unit tests for get_debug_status. Use unittest.mock.Mock to mock the ConfigLoader object. Configure the mock load_config method to return different dictionaries or raise FileNotFoundError to test all scenarios.
"""
