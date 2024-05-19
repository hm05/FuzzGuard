#!/usr/bin python3
import os
import argparse

# os.system('pip3 install -r requirements.txt')

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
    http_parser.add_argument('-p', '--password', required=False, type=str, help='Password')
    http_parser.add_argument('-P', '--passwordfile', type=argparse.FileType('r'), help='Password file')
    http_parser.add_argument('-userlabel',default="username", type=str, help='User label for form')
    http_parser.add_argument('-passlabel',default="password", type=str, help='Password label for form')
    http_parser.add_argument('--error', nargs='+', type=str, help='Error message for invalid login attempt')
    
    # FTP subparser
    ftp_parser = subparsers.add_parser('ftp', help='Specify service as FTP')
    ftp_parser.add_argument('-u', '--user',required=False, type=str, help='Username')
    ftp_parser.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')
    ftp_parser.add_argument('-P', '--password', type=argparse.FileType('r'), help='Password file')
    ftp_parser.add_argument('-host',type=str, help='Host')
    ftp_parser.add_argument('-port',default=21,type=int, help='Port')

    # Add FTP parameters here if needed

    # SSH subparser
    ssh_parser = subparsers.add_parser('ssh', help='Specify service as SSH')
    ssh_parser.add_argument('-u','--user',type=str,required=False, help='Username')
    ssh_parser.add_argument('-U','--userfile',type=argparse.FileType('r'), help='User file')
    ssh_parser.add_argument('-P','--password',type=argparse.FileType('r'), help='Password')
    ssh_parser.add_argument('-host',type=str, help='Host')
    ssh_parser.add_argument('-port',default=22,type=int, help='Port')


    # Add SSH parameters here if needed

    # SMB subparser
    smb_parser = subparsers.add_parser('smb', help='Specify service as SMB')
    smb_parser.add_argument('-port', default=445, type=int, help='Port')
    smb_parser.add_argument('-s','--share',type=str,help='Name of SMB Share')

    group_smb_pass = smb_parser.add_mutually_exclusive_group(required=True)
    group_smb_pass.add_argument('-P', '--passwordfile', type=argparse.FileType('r'), help='Password file')
    group_smb_pass.add_argument('-p', '--password', type=str, help='Password')

    group_smb_user = smb_parser.add_mutually_exclusive_group(required=True)
    group_smb_user.add_argument('-u', '--user', type=str, help='Username')
    group_smb_user.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')
    
    # Add SMB parameters here if needed

    # MySQL subparser
    mysql_parser = subparsers.add_parser('mysql', help='Specify service as MySQL')
    mysql_parser.add_argument('-H', '--host', type=str, help='Host')
    mysql_parser.add_argument('-u', '--user', type=str, help='Username')
    mysql_parser.add_argument('-p', '--password', type=str, help='Password')
    mysql_parser.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User File')
    mysql_parser.add_argument('-P', '--passfile', type=argparse.FileType('r'), help='Password File')

    # Directory subparser
    directory_parser = subparsers.add_parser('directory', help='Perform Directory Fuzzing')
    # Add Directory parameters here if needed

    # Subdomain subparser
    subdomain_parser = subparsers.add_parser('subdomain', help='Perform Subdomain Fuzzing')
    subdomain_parser.add_argument('-T', '--target', type=str, help='Specify Target')
    subdomain_parser.add_argument('-F', '--file', type=argparse.FileType('r'), help='Subdomain file')

    args = parser.parse_args()

    if args.method == 'http':
        if args.user:
            if args.passwordfile:
                os.system('python3 ./FuzzHTTP.py -u {} -P {} -t {} -userlabel {} -passlabel {} -e {}'.format(args.user, args.passwordfile.name, args.target, args.userlabel, args.passlabel, args.error))
            else:
                os.system('python3 ./FuzzGuard.py -h')
        else:
            if args.password:
                os.system('python3 ./FuzzHTTP.py -U {} -p {} -t {} --error {}'.format(args.userfile.name, args.password, args.target,args.error))
            elif args.passwordfile:
                os.system('python3 ./FuzzHTTP.py -U {} -P {} -t {} --error {}'.format(args.userfile.name, args.passwordfile.name, args.target,args.error))
            else:
                os.system('python3 ./FuzzGuard.py -h')

    elif args.method == 'ftp':
        if args.user:
            os.system('python ./FuzzFTP.py -u {} -P {} -host {} -port {}'.format(args.user, args.password.name, args.host, args.port))
        else:
            os.system('python ./FuzzFTP.py -U {} -P {} -host {} -port {}'.format(args.userfile.name, args.password.name, args.host, args.port))



    elif args.method == 'ssh':
        if args.user:
            os.system('python ./FuzzSSH.py -u {} -P {} -host {} -port {}'.format(args.user, args.password.name, args.host, args.port))
        else:
            os.system('python ./FuzzSSH.py -U {} -P {} -host {} -port {}'.format(args.userfile.name, args.password.name, args.host, args.port))
        

    elif args.method == 'smb':
        # Add SMB method handling here
        if args.user:
            if args.passwordfile:
                os.system('python3 ./FuzzSMB.py -u {} -P {} -T {} -port {}'.format(args.user, args.passwordfile.name, args.target, args.port))
        elif args.userfile:
            if args.password:
                os.system('python3 ./FuzzSMB.py -U {} -p {} -T {} -port {}'.format(args.userfile.name, args.password, args.target, args.port))
            else:
                os.system('python3 ./FuzzSMB.py -U {} -P {} -T {} -port {}'.format(args.userfile.name, args.passwordfile.name, args.target, args.port))
        else:
            os.system('python3 ./FuzzGuard.py -h')


    elif args.method == 'mysql':
        pass
        # Add MySQL method handling here

    elif args.method == 'directory':
        os.system('python3 ./FuzzDir.py -U {}'.format(args.target))

    elif args.method == 'subdomain':
        if args.file:
            os.system('python3 ./FuzzSubD.py -t {} -f {}'.format(args.target, args.file.name))
        else:
            os.system('python3 ./FuzzSubD.py -t {}'.format(args.target))

if __name__ == '__main__':
    main()
