import os
import argparse

os.system('pip install -r requirements.txt')

def main():
    """A simple VAPT tool developed by Harsh and Niral. Contribute on GitHub: https://github.com/hm05/FuzzGuard"""
    
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description='This is a simple VAPT tool developed and managed by Harsh and Niral.')

    # Add subparsers for each method
    subparsers = parser.add_subparsers(dest='method', help='Specify service')

    # HTTP subparser
    http_parser = subparsers.add_parser('http', help='Specify service as HTTP')
    http_parser.add_argument('-u', '--user',required=False, type=str, help='Username')
    http_parser.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')
    http_parser.add_argument('-P', '--passwordfile', type=argparse.FileType('r'), help='Password file')
    http_parser.add_argument('-userlabel', type=str, help='User label for form')
    http_parser.add_argument('-passlabel', type=str, help='Password label for form')
    http_parser.add_argument('-e', '--error', type=str, help='Error message for invalid login attempt')
    
    # FTP subparser
    ftp_parser = subparsers.add_parser('ftp', help='Specify service as FTP')

    # Add FTP parameters here if needed

    # SSH subparser
    ssh_parser = subparsers.add_parser('ssh', help='Specify service as SSH')
    # Add SSH parameters here if needed

    # SMB subparser
    smb_parser = subparsers.add_parser('smb', help='Specify service as SMB')
    # Add SMB parameters here if needed

    # MySQL subparser
    mysql_parser = subparsers.add_parser('mysql', help='Specify service as MySQL')
    # Add MySQL parameters here if needed

    # Directory subparser
    directory_parser = subparsers.add_parser('directory', help='Perform Directory Fuzzing')
    # Add Directory parameters here if needed

    # Subdomain subparser
    subdomain_parser = subparsers.add_parser('subdomain', help='Perform Subdomain Fuzzing')
    # Add Subdomain parameters here if needed
    parser.add_argument('-T', '--target', type=str, help='Specify Target')

    args = parser.parse_args()

    if args.method == 'http':
        if args.user:
            if args.passwordfile:
                os.system('python ./FuzzHTTP.py -u {} -P {} -t {} -userlabel {} -passlabel {} -e {}'.format(args.user, args.passwordfile.name, args.target, args.userlabel, args.passlabel, args.error))
            else:
                os.system('python ./FuzzGuard.py -h')
        else:
            if args.password:
                os.system('python ./FuzzHTTP.py -U {} -p {} -t {}'.format(args.userfile.name, args.password, args.target))
            elif args.passwordfile:
                os.system('python ./FuzzHTTP.py -U {} -P {} -t {}'.format(args.userfile.name, args.passwordfile.name, args.target))
            else:
                os.system('python ./FuzzGuard.py -h')

    elif args.method == 'ftp':
        pass
        # Add FTP method handling here

    elif args.method == 'ssh':
        print("ssh")
        

    elif args.method == 'smb':
        pass
        # Add SMB method handling here

    elif args.method == 'mysql':
        pass
        # Add MySQL method handling here

    elif args.method == 'directory':
        os.system('python ./FuzzDir.py -U {}'.format(args.target))

    else:
        os.system('python ./FuzzSubD.py -U {}'.format(args.target))

if __name__ == '__main__':
    main()
