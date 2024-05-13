import argparse
import mysql.connector

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MySQL Connector')
    user = parser.add_mutually_exclusive_group(required=True)
    user.add_argument('-u', '--user', type=str, help='Username')
    user.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User File')
    password = parser.add_mutually_exclusive_group(required=True)
    password.add_argument('-p', '--password', type=str, help='Password')
    password.add_argument('-P', '--passfile', type=argparse.FileType('r'), help='Password File')
    parser.add_argument('-H', '--host', type=str, help='Host')
    args = parser.parse_args()
    if args.user:
        if args.passwordfile:
            mydb = mysql.connector.connect(
              host=args.host,
              user=args.user,
              password=args.passwordfile.name
            )
        else:
            mydb = mysql.connector.connect(
              host=args.host,
              user=args.user,
              password=args.password
            )
    else:
        if args.password:
            mydb = mysql.connector.connect(
              host=args.host,
              user=args.userfile.name,
              password=args.password
            )
        elif args.passwordfile:
            mydb = mysql.connector.connect(
              host=args.host,
              user=args.userfile.name,
              password=args.passwordfile.name
            )