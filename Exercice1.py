# print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star,\n\t How I wonder what you are")


### Mini exo fonction

def nblettre(mot):
    maj = 0
    min = 0
    
    for i in range (len(mot)):
        if (ord(mot[i]) >= 97 and ord(mot[i]) <= 122) :
            min += 1
    
        elif (ord(mot[i]) >= 65 and ord(mot[i]) <= 90) :
            maj += 1
        

    print(f'Nombre de minuscules = {min} \nNombre de majuscules = {maj}')