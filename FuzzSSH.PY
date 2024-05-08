import os
import argparse
import paramiko

parser = argparse.ArgumentParser(description='SSH Bruteforce')
parser.add_argument('-u','--user',type=str,required=False, help='Username')
parser.add_argument('-p','--password',type=str,required=False, help='Password')
parser.add_argument('-U','--userfile',type=argparse.FileType('r'), help='User file')
parser.add_argument('-P','--password',type=argparse.FileType('r'), help='Password')
parser.add_argument('-h','--host',type=str, help='Host')
parser.add_argument('-port',type=int,default=22, help='Port')

args = parser.parse_args()

print(args.user)
print(args.password)
print(args.userfile)
print(args.passwordfile)
print(args.host)
print(args.port)


