"""
Mocking a Logger for an Application:

    Imagine you have a process_data(data) function that internally uses a Logger class (which you don't need to define fully, just assume it exists and has a log_info(message) method).

    The process_data function should call logger.log_info("Processing data...") at the start and logger.log_info("Data processed successfully.") at the end.

    Using @patch (or Mock if the Logger is passed as an argument), mock the Logger within a test for process_data.
    Assert that log_info was called with the correct messages and the correct number of times.
"""

import unittest
from unittest.mock import call, patch, Mock


# class Logger:
#     def log_info(self, message):
#         print(message)


def process_data(logger):
    logger.log_info("Processing data ...")
    logger.log_info("Data processed successfully.")


class TestLoggerClass(unittest.TestCase):
    def test_proccess_data(self):
        mock_log = Mock()
        process_data(mock_log)

        # Assertions
        self.assertEqual(mock_log.log_info.call_count, 2)
        mock_log.log_info.assert_has_calls(
            [call("Processing data ..."), call("Data processed successfully.")]
        )


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
