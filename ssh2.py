import paramiko

host = "192.168.1.16"
port = 22
transport = paramiko.Transport((host, port))

password = "debian"
username = "root"
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

source_folder = "C:\Users\sylva\OneDrive\Bureau\Scripting systeme\Python\miniTP1.py"
inbound_files = sftp.listdir(source_folder)

