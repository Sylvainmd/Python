# with open("text.txt", "a") as f:
#     f.write("Hello World\n")


# import sys

# fichier, content, fin, nombre = sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4]
# nb = int(nombre)
# with open(fichier, "a") as f:
#     while nb < 0 :
#         f.write(content)
#         nb-=1
    
#     f.write(fin)
    
import sys

fichier, content, fin, nombre = sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4]

nb = int(nombre)
with open(fichier, "a") as f:
    while nb > 0 :
        f.write(content)
        nb-=1

    f.write(fin)