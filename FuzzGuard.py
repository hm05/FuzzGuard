import os
import argparse

os.system('pip install -r requirements.txt')

def main():
    """A simple VAPT tool developed by Harsh and Niral. Contribute on GitHub: https://github.com/hm05/FuzzGuard"""
    
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='This is a simple VAPT tool developed and managed by Harsh and Niral.')

    parser.add_argument('-T', '--target', type=str, help='Specify Target')
    # Add mutually exclusive groups for specifying the method, user, and password
    group_method = parser.add_mutually_exclusive_group(required=True)
    group_method.add_argument('-H', '--http', action='store_true', help='Specify service as HTTP')
    group_method.add_argument('-f', '--ftp', action='store_true', help='Specify service as FTP')
    group_method.add_argument('-s', '--ssh', action='store_true', help='Specify service as SSH')
    group_method.add_argument('-S', '--smb', action='store_true', help='Specify service as SMB')
    group_method.add_argument('-M', '--mysql', action='store_true', help='Specify service as MySQL')
    group_method.add_argument('-D', '--directory', action='store_true', help='Perform Directory Fuzzing')
    group_method.add_argument('-F', '--subdomain', action='store_true', help='Perform Subdomain Fuzzing')

    group_user = parser.add_mutually_exclusive_group(required=True)
    group_user.add_argument('-u', '--user', type=str, help='Username')
    group_user.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')

    group_password = parser.add_mutually_exclusive_group(required=True)
    group_password.add_argument('-p', '--password', type=str, help='Password')
    group_password.add_argument('-P', '--passwordfile', type=argparse.FileType('r'), help='Password file')

    args = parser.parse_args()

    if args.http:
        if args.user:
            if args.password:
                os.system('python ./FuzzHTTP.py -u {} -p {}'.format(args.user, args.password))
            elif args.passwordfile:
                os.system('python ./FuzzHTTP.py -u {} -P {}'.format(args.user, args.passwordfile.name))
            else:
                os.system('python ./FuzzGuard.py -h')
        
        elif args.userfile:
            if args.password:
                os.system('python ./FuzzHTTP.py -U {} -p {}'.format(args.userfile.name, args.password))
            elif args.passwordfile:
                os.system('python ./FuzzHTTP.py -U {} -P {}'.format(args.userfile.name, args.passwordfile.name))
            else:
                os.system('python ./FuzzGuard.py -h')

        else:
            os.system('python ./FuzzGuard.py -h')

    if args.ftp:
        os.system()

    if args.ssh:
        os.system()

    if args.smb:
        os.system()

    if args.mysql:
        os.system()

    if args.directory:
        os.system('python ./FuzzDir.py -U {}'.format(args.target))

    if args.subdomain:
        os.system('python ./FuzzSubD.py -U {}'.format(args.target))

if __name__ == '__main__':
    main()
