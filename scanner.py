import socket # For connecting to the target IP
# from network_info import ip separate file with ip for static ip
# ip = ip

def get_ip_address():
    # Get the hostname
    hostname = socket.gethostname()
    # Get the IP address using the hostname
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Get and print the IP address
print(get_ip_address())

# create a class called PortScanner with target ip bounds
class PortScanner:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

# create a method called scan that will scan the target ip and return open ports
    def scan(self):
        """Scan the specified ports of the target IP."""
        open_ports = []
        for port in range(self.start_port, self.end_port + 1):
            if self._is_open(port):
                open_ports.append(port)
        return open_ports

# used in the scan method to check if a port is open
    def _is_open(self, port):
        """Check if a given port is open."""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket
        s.settimeout(1)  # One second timeout
        result = s.connect_ex((self.target_ip, port))
        s.close()
        return result == 0

# create a scanner object and print the open ports
start_port = 1
end_port = 65535
target_ip = get_ip_address()
if __name__ == '__main__':
    scanner = PortScanner(target_ip, start_port, end_port)
    open_ports = scanner.scan()
    print(f'Open ports: {open_ports}')
