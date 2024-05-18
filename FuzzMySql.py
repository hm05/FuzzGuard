import argparse
import mysql.connector

def connectMySQL(host, user, password, userfile=None, passfile=None):
    try:
        if userfile and passfile:
            with open (userfile, 'r') as userfile:
                users =  userfile.readlines()

            with open (passfile, 'r') as passfile:
                passwords = passfile.readlines()

            for user in users:
                user = user.strip()
                for password in passwords:
                    password = password.strip()
                    try:
                        mydb = mysql.connector.connect(
                            host=host,
                            user=user,
                            password=password
                        )
                        mydb.close()
                        print(f'\033[92m [+]\033[0m {user} : ', password)
                        break

                    except mysql.connector.Error as err:
                        print(f'\033[91m [-]\033[0m {user} : ', password)

        elif user and passfile:
            with open (passfile, 'r') as f:
                passwords = f.readlines()
            
            for password in passwords:
                try:
                    mydb = mysql.connector.connect(
                        host=host,
                        user=user,
                        password=password
                    )
                    mydb.close()
                    print(f'[\033[92m + \033[0m] Successfully connected to MySQL database: {user}@{host}')

                except mysql.connector.Error as err:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        elif password and userfile:
            with open (userfile, 'r') as userfile:
                users = userfile.readlines()

            for user in users:
                try:
                    mydb = mysql.connector.connect(
                        host=host,
                        user=user,
                        password=password
                    )
                    mydb.close()
                    print(f'[\033[92m + \033[0m] Successfully connected to MySQL database: {user}@{host}')

                except mysql.connector.Error as err:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

    except KeyboardInterrupt:
        print('\033[[91m - \033[0m] Detecting Keyboard Interrupt...Exiting...')
        exit(1)

def main():
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


    if args.userfile:
        userfile = args.userfile.name
    else:
        userfile = None

    if args.passfile:
        passfile = args.passfile.name
    else:
        passfile = None

    print(f'\033[0;34m [*] \033[0m MySQL Connector')
    print(f'\033[0;34m [*] \033[0m Host: {args.host}')
    print(f'\033[0;34m [*] \033[0m User: {args.user}')
    print(f'\033[0;34m [*] \033[0m Password: {args.password}')
    print(f'\033[0;34m [*] \033[0m User File: {userfile}')
    print(f'\033[0;34m [*] \033[0m Password File: {passfile}')

    connectMySQL(args.host, args.user, args.password, userfile, passfile)

    
if __name__ == '__main__':
    main()
