#!/usr/bin python3
import os
import argparse
import FuzzSMB
import FuzzHTTP
import FuzzFTP
import FuzzSSH
import FuzzMySql
import FuzzDir
import FuzzSubD

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
    ftp_parser.add_argument('-P', '--passwordfile', type=argparse.FileType('r'), help='Password file')
    ftp_parser.add_argument('-p', '--password', type=str, help='Password')
    ftp_parser.add_argument('-port',default=21,type=int, help='Port')

    # Add FTP parameters here if needed

    # SSH subparser
    ssh_parser = subparsers.add_parser('ssh', help='Specify service as SSH')
    ssh_parser.add_argument('-u','--user',type=str,required=False, help='Username')
    ssh_parser.add_argument('-U','--userfile',type=argparse.FileType('r'), help='User file')
    ssh_parser.add_argument('-P','--passwordfile',type=argparse.FileType('r'), help='Password file')
    ssh_parser.add_argument('-p','--password',type=argparse.FileType('r'), help='Password')
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
    
  

    # MySQL subparser
    mysql_parser = subparsers.add_parser('mysql', help='Specify service as MySQL')
    mysql_parser.add_argument('-u', '--user', type=str, help='Username')
    mysql_parser.add_argument('-p', '--password', type=str, help='Password')
    mysql_parser.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User File')
    mysql_parser.add_argument('-P', '--passfile', type=argparse.FileType('r'), help='Password File')

    # Directory subparser
    directory_parser = subparsers.add_parser('directory', help='Perform Directory Fuzzing')
    directory_parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Fuzzing File', required=False)

    # Subdomain subparser
    subdomain_parser = subparsers.add_parser('subdomain', help='Perform Subdomain Fuzzing')
    subdomain_parser.add_argument('-F', '--file', type=argparse.FileType('r'), help='Subdomain file')

    parser.add_argument('-T', '--target', type=str, help='Specify Target', required=False)

    args = parser.parse_args()



    if args.method == 'http':
        
        userfile = None if not args.userfile else args.userfile.name
        passwordfile = None if not args.passwordfile else args.passwordfile.name

        FuzzHTTP.http_bruteforce(args.target, args.userlabel, args.passlabel, userfile, passwordfile, args.error, args.user, args.password)



    elif args.method == 'ftp':
       
        userfile = None if not args.userfile else args.userfile.name
        passwordfile = None if not args.passwordfile else args.passwordfile.name

        FuzzFTP.bruteFTP(args.target, userfile, passwordfile, args.user, args.password)



    elif args.method == 'ssh':
        
        userfile = None if not args.userfile else args.userfile.name
        passwordfile = None if not args.passwordfile else args.passwordfile.name

        FuzzSSH.ssh_bruteforce(args.target, args.port, userfile, passwordfile, args.user, args.password)



    elif args.method == 'smb':
    
        userfile = None if not args.userfile else args.userfile.name
        passwordfile = None if not args.passwordfile else args.passwordfile.name

        FuzzSMB.fuzz_smb(args.user,args.password,args.target, args.share,  args.port, userfile, passwordfile)



    elif args.method == 'mysql':
         
        userfile = None if not args.userfile else args.userfile.name
        passwordfile = None if not args.passfile else args.passfile.name

        FuzzMySql.connectMySQL(args.target, args.user, args.password, userfile, passwordfile)


    elif args.method == 'directory':

        FuzzDir.fuzz(args.target, args.file.name) if args.file else FuzzDir.fuzz(args.target)
        

    elif args.method == 'subdomain':

        FuzzSubD.fuzz(args.target, args.file.name) if args.file else FuzzSubD.fuzz(args.target)

if __name__ == '__main__':
    main()
