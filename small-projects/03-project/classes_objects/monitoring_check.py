"""
Monitoring Service Check:

    Define a class MonitoringService with an __init__ method that accepts a list of servers (these can be simple strings for this exercise).

    Add a method check_all_servers(self) that iterates through the servers list. For each server, it should conceptually "check" its status. In this exercise, instead of actually checking, it should print a message like "Checking server: [server_name]".

    Create a function run_monitoring_cycle(service_instance) that takes a MonitoringService object and calls its check_all_servers method.

    Write a unit test for run_monitoring_cycle. Use @patch to mock the MonitoringService class (or pass a Mock object directly). Configure the mock MonitoringService to ensure its check_all_servers method is called correctly when run_monitoring_cycle is executed.
"""

import unittest
from unittest import mock
from unittest.mock import Mock, patch, call


class MonitoringService:
    def __init__(self, server_list):
        self.server_list = server_list

    def check_all_servers(self):
        for server in self.server_list:
            print(f"Checking Server: '{server}'")


def run_monitoring_cycle(service_instance):
    """
    Takes monitoring service object and calls it's methods
    """
    service_instance.check_all_servers()


my_servers = ["srv-01", "srv-02", "srv-03", "srv-04", "srv-05"]
monitoring_list = MonitoringService(my_servers)

# run_monitoring_cycle(monitoring_list)


class TestMonitoringService(unittest.TestCase):
    """
    Test suite for the MonitoringService class and related functions.
    """

    def test_run_monitoring_cycle_triggers_check(self):
        """
        Test that run_monitoring_cycle successfully calls check_all_servers on the injected service.
        """
        mock_monitor_list = Mock()
        run_monitoring_cycle(mock_monitor_list)
        mock_monitor_list.check_all_servers.assert_called_once_with()

    @patch("builtins.print")
    def test_check_all_servers_loop(self, mock_print):
        # 2. The REAL System: Build a real object with a real list
        test_servers = ["srv-100", "srv-200"]
        real_service = MonitoringService(test_servers)

        # 3. The Action: Run the real method
        # This will trigger the 'for' loop, which will try to call print()
        real_service.check_all_servers()

        # 4. The Receipts: Check the mock_print's notebook!
        expected_calls = [
            call("Checking Server: 'srv-100'"),
            call("Checking Server: 'srv-200'"),
        ]
        mock_print.assert_has_calls(expected_calls)

        # Bonus check: Prove it ONLY looped twice
        self.assertEqual(mock_print.call_count, 2)


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
