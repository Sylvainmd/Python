import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",1234))

server.listen()

client, addr = server.accept()

termine = False

while not termine:
    msg = client.recv(1024).decode('utf-8')
    if msg =='quit':
        termine == True
    else:
        print(msg)
        
    client.send(input("Message: ").encode('utf-8'))
        