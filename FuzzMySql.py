import argparse
import mysql.connector

def connectMySQL(host, user, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print(f'[\033[92m + \033[0m] Successfully connected to MySQL database: {user}@{host}')
        return mydb
    except mysql.connector.Error as err:
        print(f'[\033[91m - \033[0m] Failed to connect to MySQL database: {err}')
        return None
    except KeyboardInterrupt:
        print('[\033[91m - \033[0m] Detecting Keyboard Interrupt...Exiting...')
        exit(1)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MySQL Connector')
    parser.add_argument('-u', '--user', type=str, help='Username')
    parser.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User File')
    parser.add_argument('-p', '--password', type=str, help='Password')
    parser.add_argument('-P', '--passfile', type=argparse.FileType('r'), help='Password File')
    parser.add_argument('-H', '--host', type=str, help='Host')
    args = parser.parse_args()

    if not args.user and not args.userfile:
        parser.error('Please provide a username or a file containing usernames.')

    if not args.password and not args.passfile:
        parser.error('Please provide a password or a file containing passwords.')

    user = args.user if args.user else args.userfile.readline().strip()
    password = args.password if args.password else args.passfile.readline().strip()

    mydb = connectMySQL(args.host, user, password)
