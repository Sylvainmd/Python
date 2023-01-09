import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind(("localhost",1234))

termine = False

while not termine:
    client.send(input("Message :").encode('utf-8'))
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        termine = True
    if msg == 'exec':
        print("j'execute ma commande")
    
    client.send(input("Message: ").encode('utf-8'))