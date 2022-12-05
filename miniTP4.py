# with open("text.txt", "a") as f:
#     f.write("Hello World\n")


import sys

fichier, content = sys.argv[1], sys.argv[2]
with open(fichier, "a") as f:
    f.write(content)