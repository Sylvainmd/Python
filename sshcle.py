import paramiko

ssh = paramiko.SSHClient()

ssh.connect('192.168.10.10', username='sylvain', key_filename="C:\\Users\sylva\.ssh\id_rsa")

stdin, stdout, stderr = ssh.exec_command('ls -l')

print(stdout.readlines())

ssh.close()