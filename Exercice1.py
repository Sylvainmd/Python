#ecrire un programme qui prend un emoji et qui l'ecrit dans le terminal le nombre de fois voulu.
#Ce nombre doit etre compris entre 3 et max 15, en default il le met 5 fois si l'utilisateur ne rentre rien


import argparse

valeur = argparse.ArgumentParser(
                    prog = "Mon programme",
                    description = 'Répéter une valeur',
                    )

valeur.add_argument('filename')
valeur.add_argument('-m', '--message')
valeur.add_argument('-r', '--repetition',type=int, default=5, choices=range(3,15))

args = valeur.parse_args()
print(args.filename, args.message, args.repetition)

nb = int(args.repetition)
with open(args.filename, "a") as f:    
    for i in range(0,int(args.repetition)):

        f.write(args.message)
        nb-=1