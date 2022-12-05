import os
import sys

print(sys.argv[0])

liste = os.listdir(sys.argv[1])

for nb,i in enumerate(liste):

    print(f"{nb}. {i}")

print(liste)