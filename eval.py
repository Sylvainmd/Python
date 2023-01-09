# import sys

# fichier, nom, age = sys.argv[1], sys.argv[2], sys.argv[3]

# with open(fichier, "a") as f:
#     f.write(f"{nom} {age}")


# import argparse
# import os

# valeur = argparse.ArgumentParser(
#                     prog = "Mon programme",
#                     description = 'search / replace',
#                     )

# valeur.add_argument('filename')
# valeur.add_argument('-s', '--search')
# valeur.add_argument('-r', '--replace')

# args = valeur.parse_args()
# print(args.filename, args.search, args.replace)

# line = []
# with open(args.filename, "r") as f:    
#         line =f.read()
# # print(line)


# new_line = line.replace(args.search, args.replace)
        
# # print(line)        
# with open(args.filename, "w") as r: 
#         r.write(new_line)

# # print(line)



# import argparse

# valeur = argparse.ArgumentParser(
#                     prog = "Mon programme",
#                     description = 'Répéter age',
#                     )

# valeur.add_argument('filename')
# valeur.add_argument('-a', '--age')
# valeur.add_argument('-r', '--repetition',type=int, default=5)

# args = valeur.parse_args()
# print(args.filename, args.age, args.repetition)

# nb = int(args.repetition)
# with open(args.filename, "a") as f:    
#     for i in range(0,int(args.repetition)):

#         f.write(f"{args.age}\n")
#         nb-=1

# def hello():
#    print("hello world")
   
# hello()







import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('192.168.1.16', username='root', password="debian")


stop = False
chan = ssh.invoke_shell()
while not stop:
    commande = input("Entrez la commande : ")
    if commande == stop:
        stop = True
        
    stdin, stdout, stderr = ssh.exec_command(commande) 

    print(stdout.read())
    
chan.close()
ssh.close()