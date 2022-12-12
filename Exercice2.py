#recherche un mot dans un fichier et remplace toutes les occurences par un autre mot

import argparse
import os

valeur = argparse.ArgumentParser(
                    prog = "Mon programme",
                    description = 'Rechercher / Remplacer',
                    )

valeur.add_argument('filename')
valeur.add_argument('-s', '--search')
valeur.add_argument('-r', '--replace')

args = valeur.parse_args()
print(args.filename, args.search, args.replace)

line = []
with open(args.filename, "r") as f:    
        line =f.read()
# print(line)


new_line = line.replace(args.search, args.replace)
        
# print(line)        
with open(args.filename, "w") as r: 
        r.write(new_line)

# print(line)