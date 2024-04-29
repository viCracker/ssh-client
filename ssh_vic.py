import paramiko


def ssh_command(ip_addr, port, user_name, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip_addr, port=port, username=user_name, password=passwd)

    _, stdout, stderr = client.exec_command(command)
    output = stdout.readlines() + stderr.readlines()
    if output:
        for line in output:
            print(line.strip())


if __name__ == "__main__":
    try:
        import getpass
        # user = getpass.getuser()
        print("Tool: viCracker SSH Client")
        user_name = input("username: ")
        password = getpass.getpass()

        ip_addr = input("Enter server IP: ")
        port = input("Enter port: ")
        on = True
        while on:
            cmd = input("$ ")
            ssh_command(ip_addr, port, user_name, password, cmd)
    except KeyboardInterrupt:
        print("Session Closed")
