#recherche un mot dans un fichier et remplace toutes les occurences par un autre mot

import argparse


valeur = argparse.ArgumentParser(
                    prog = "Mon programme",
                    description = 'Rechercher / Remplacer',
                    )

valeur.add_argument('filename', type=str)
valeur.add_argument('-s', '--search')
valeur.add_argument('-r', '--replace')

args = valeur.parse_args()
print(args.filename, args.search, args.replace)

with open(args.filename, "w") as f:    
    for i in args.filename :
        line = f.read()
        print (line)
        if line == args.search :
            f.write(args.replace)
            i += 1
        else :
            i += 1