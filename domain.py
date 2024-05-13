import socket

def domain_exists(domain):
    try:
        # Resolve the domain name to an IP address
        ip_address = socket.gethostbyname(domain)
        print(f"Domain '{domain}' exists. IP Address: {ip_address}")
        return True
    except socket.gaierror:
        print(f"Domain '{domain}' does not exist.")
        return False

# Example usage:
domain_exists("www.google.com")
