import argparse
import requests

def fuzz(target, file = './small.txt'):
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Directory Fuzzing')
    target_url = parser.add_mutually_exclusive_group(required=True)
    target_url.add_argument('-t', '--target', type=str, help='Target URl')
    target_url.add_argument('-f', '--file', type=str, help='Fuzzing File')
    args = parser.parse_args()
    
    if args.file == None:
        fuzz(args.target)
    else:
        fuzz(args.target, args.file)