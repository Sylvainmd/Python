import os
import sys

print(sys.argv[0])

liste = os.listdir("C:\\Users")

for nb,i in enumerate(liste):

    print(f"{nb}. {i}")

print(liste)