import os
import sys


directory_input, mon_prenom, age = sys.argv[1], sys.argv[2], sys.argv[3]

print(f"path : {directory_input}, mon prenom: {mon_prenom}, mon age :  {age}")

list_dir = os.listdir(directory_input)


for number, directory in enumerate(list_dir):
    print(f"{number}. : {directory}")
print(f"Le contenu de mon répertoire : {list_dir}")