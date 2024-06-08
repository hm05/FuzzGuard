import requests
import argparse

def fuzz(target, file = 'small.txt'):
    try:
        with open(file, 'r') as f:
            for word in f.readlines():
                word = word.strip()
                response = requests.get(target + '/' + word)
                if response.status_code == 200:
                    print(f'\033[92m [+]\033[0m Found: {target}/{word}')
                # else:
                #     print(f'\033[91m [-]\033[0m Not Found: {target}/{word}')
    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)

