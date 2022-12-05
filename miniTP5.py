import sys
# import os

fichier, content, fin= sys.argv[1], sys.argv[2], sys.argv[3]
# print(len(sys.argv))
if len(sys.argv) >=5:
    nombre = sys.argv[4]
    nb = int(nombre)

try:
    with open(fichier, "a") as f:
        if len(sys.argv) >=5:
            while nb > 0 :
                f.write(f"{content}\n")
                nb-=1
        else:
            f.write(f"{content}\n")
            
        f.write(fin)
except:
    print("error write")


# try:
#     with open(fichier, "a") as f:
#         print(fichier)
# except:
#     print("error read")