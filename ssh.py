import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.1.16', username='root', password="debian")

stdin, stdout, stderr = ssh.exec_command('ls -l')

print(stdout.readlines())

ssh.close()