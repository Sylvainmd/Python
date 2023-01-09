import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.1.16', username='Sylvain', password="Sylvian$C87")

sftp = paramiko.SFTPClient.from_transport(transport)

source_folder = "C:\Users\sylva\OneDrive\Bureau\Scripting systeme\Python\creacompte.txt"
inbound_files = sftp.listdir(source_folder)

ssh.close()

print("Création utilisateur fini")