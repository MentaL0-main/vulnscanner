import sys
import socket
import requests

class Scanner:
    def __init__(self, argv):
        if len(argv) < 2:
            self.show_help()
            exit()

        self.url = argv[1]
    
    def scan_port(self, target, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0

    def check_open_ports(self):
        start_port = 1
        end_port = 9999
        open_ports = []

        print("[:|] Scanning open ports...")

        for port in range(start_port, end_port + 1):
            print(f"[:|] Check {port} for opened\r", end="")
            if self.scan_port(self.url, port):
                open_ports.append(port)

        if (len(open_ports) > 0):
            print("[:)] open ports: ", open_ports)
        else:
            print("[:(] No opened ports.")

    def check_for_xss(self):
        payload = "<script>alert('XSS');</script>"

        fields = ['input_field1', 'input_field2']

        for field in fields:
            response = requests.post(url, data={field: payload})

            if payload in response.text:
                print("[:)] XSS maybe work.")
                return

        print("[:(] No XSS work.")

    def scan(self):
        self.check_open_ports()
        self.check_for_xss()

    def show_help(self):
        print("[:|] Usage: python3 scanner.py target-url")
    
if __name__ == "__main__":
    scanner = Scanner(sys.argv);
    scanner.scan();
