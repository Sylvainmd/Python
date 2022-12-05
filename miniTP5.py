import sys

fichier, content, fin= sys.argv[1], sys.argv[2], sys.argv[3]
if sys.argv[4] is not None:
    nombre = sys.argv[4]
    nb = int(nombre)

try:
    with open(fichier, "a") as f:
        if nb is not None:
            while nb > 0 :
                f.write(content,"\n")
                nb-=1
        else:
            f.write(content)
            
        f.write(fin)
except:
    print("error")