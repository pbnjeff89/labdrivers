import socket
import visa

class SwitchMatrix708B:
    """
    Create an object that uses the Keithley 708B Switching Matrix.

    Currently supports VISA and LAN control.

    :param str mode: The mode of operation, can be either 'visa' or 'ip' (default: 'visa')
    :param str resource_name: VISA resource name(default: None)
    :param str ip_address: IP address (default: None)
    :param int port: Port number (default: 5025)
    :param float timeout: Time to wait for a response in seconds (default: 10.0)
    :param int bytes_to_read: Number of bytes to read from the 708B (default: 2048)
    """
    __init__(self, mode: str='visa', resource_name: str=None, ip_address: str=None, port: int=5025,
             timeout: float=10.0, bytes_to_read: int=2048):
        self.mode = mode
        self.resource_name = resource_name
        self.ip_address = ip_address
        self.port = port
        self.timeout = timeout
        self.bytes_to_read = bytes_to_read