import unittest
from unittest import mock
from unittest.mock import patch, Mock


class Server:
    def __init__(self, hostname, ip_address, status="online"):
        """
        Initializes a Server object.

        Args:
            hostname (str): The network name of the server.
            ip_address (str): The IP address of the server.
            status (str): The current operational status of the server (e.g., "online", "offline").
                          Defaults to "online".
        """

        self.hostname = hostname
        self.ip_address = ip_address
        self.status = status

    def ping_server(self):
        """
        Simulates attempting to ping the server.
        In a real scenario, this would perform a network request.
        For this exercise, it returns a hardcoded boolean for demonstrative purposes.
        """
        return True

    def get_ping_server_string(self):
        """
        Returns a hardcoded string response for the ping, as per original exercise.
        This allows `ping_server` to return a boolean for clearer logic.
        """
        if self.ping_server():
            return "Server responded: Pong"
        else:
            return (
                "Server unreachable"  # This path won't be hit with default ping_server
            )

    def set_status(self, new_status):
        """
        Updates the operational status of the server.
        Args:
            new_status (str): The new status to set (e.g., "online", "maintenance").
        """
        self.status = new_status


def check_server_detailed_status(server):
    """
    Takes a Server object, attempts to ping it, and returns a detailed status message.
    This function interprets the boolean result of `ping_server`.

    Args:
        server (Server): The Server object to check.

    Returns:
        str: A formatted string indicating the server's ping status.
    """
    if server.ping_server():
        return f"Server {server.hostname} ({server.ip_address}) is currently reachable."
    else:
        return (
            f"Server {server.hostname} ({server.ip_address}) is currently unreachable."
        )


# instantiation
server1 = Server("sv1", "192.168.1.1", "online")
server2 = Server("sv2", "192.168.1.2")
print(
    f"Hostaname:{server1.hostname}, Ip_address:{server1.ip_address}, Status:{server1.status} "
)

print(check_server_detailed_status(server1))


# unit test class
class TestServer(unittest.TestCase):
    """
    Test suite for the Server class and related functions.
    """

    def test_check_server_detailed_status_reachable(self):
        """
        Tests check_server_detailed_status when ping_server indicates the server is reachable.
        """
        mock_server = Mock()
        mock_server.hostname = "test_host_up"
        mock_server.ip_address = "10.0.0.1"
        mock_server.ping_server.return_value = True  # Configure mock for 'UP' scenario

        expected_status_msg = "Server test_host_up (10.0.0.1) is currently reachable."
        actual_status_msg = check_server_detailed_status(mock_server)

        self.assertEqual(actual_status_msg, expected_status_msg)
        mock_server.ping_server.assert_called_once()  # Verify ping_server was called

    def test_check_server_detailed_status_unreachable(self):
        """
        Tests check_server_detailed_status when ping_server indicates the server is unreachable.
        """
        mock_server = Mock()
        mock_server.hostname = "test_host_down"
        mock_server.ip_address = "10.0.0.2"
        mock_server.ping_server.return_value = False

        expected_status_msg = (
            "Server test_host_down (10.0.0.2) is currently unreachable."
        )
        actual_status_msg = check_server_detailed_status(mock_server)

        self.assertEqual(actual_status_msg, expected_status_msg)
        mock_server.ping_server.assert_called_once()  # Verify ping_server was called

    def test_set_status_updates_correctly(self):
        """
        Tests that the set_status method correctly updates the server's status.
        This is a direct test of the Server class itself, not involving mocks for `ping_server`.
        """
        server = Server("srv1", "10.0.0.3")
        self.assertEqual(server.status, "online")

        server.set_status("offline")
        self.assertEqual(server.status, "offline")

        server.set_status("maintenance")
        self.assertEqual(server.status, "maintenance")


# To run the test if this script is executed directly
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
