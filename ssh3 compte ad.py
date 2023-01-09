import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = "192.168.1.16"
port = 22
transport = paramiko.Transport((host, port))

username = "Sylvain"
password = "Sylvain$87"

sftp = paramiko.SFTPClient.from_transport(transport)

source_folder = "C:\Users\sylva\OneDrive\Bureau\Scripting systeme\Python\creacompte.txt"
inbound_files = sftp.listdir(source_folder)

ssh.close()

print("Création utilisateur fini")