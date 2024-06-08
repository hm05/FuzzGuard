import argparse
import socket
import re

def filter_url(url):
    """
    Removes http://www., https://www., or www. from the beginning of a URL.

    Args:
        url (str): The URL string.

    Returns:
        str: The modified URL with protocol and www removed (if present).
    """
    pattern = r"(?:https?://)?(?:www\.)?(.*)"
    match = re.match(pattern, url)
    if match:
        return match.group(1)  # Return the captured group (remaining part of URL)
    else:
        return url  # Return the original URL if no match

def fuzz(target, file='./subdomains.txt'):
    """
    Performs directory fuzzing on a target domain using a wordlist.

    Args:
        target (str): The target domain name (with protocol removed).
        file (str, optional): The path to the wordlist file. Defaults to './subdomains.txt'.
    """
    try:
        # Use the provided filename or default if not specified
        filename = file if file else './subdomains.txt'  

        with open(filename, 'r') as f:
            for word in f.readlines():
                word = word.strip()
                domain = f"{word}.{target}"

                try:
                    # Resolve the domain name to an IP address
                    ip_address = socket.gethostbyname(domain)
                    if ip_address != None:
                        print(f"[\033[92m +\033[0m ] {domain}")  # Set flag to true if domain is found

                    else:
                        print(f"[\033[91m -\033[0m ] {domain}")
                except socket.gaierror:
                    print("Socket error")  # Ignore socket errors and continue with next word

                # Print the domain along with whether it's found or not
                
                
    except KeyboardInterrupt:
        print('[\033[91m -\033[0m ] Detecting Keyboard Interrupt...Exiting...')
        exit(1)
    except FileNotFoundError:
        print(f"Error: Wordlist file '{filename}' not found.")

