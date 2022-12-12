# print("Twinkle, twinkle, little star,\n\t\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky. \n Twinkle, twinkle, little star,\n\t How I wonder what you are")


### Mini exo 1

# def nblettre(mot):
#     maj = 0
#     min = 0
    
#     for i in range (len(mot)):
#         if (ord(mot[i]) >= 97 and ord(mot[i]) <= 122) :
#             min += 1
    
#         elif (ord(mot[i]) >= 65 and ord(mot[i]) <= 90) :
#             maj += 1
        

#     print(f'Nombre de minuscules = {min} \nNombre de majuscules = {maj}')
    

##Correction

# def count_letters(string):
#   upper_count = 0
#   lower_count = 0
#   for char in string:
#     if char.isupper():
#       upper_count += 1
#     elif char.islower():
#       lower_count += 1
  
#   return upper_count, lower_count


### Mini exo 2


def maj(phrase) :
    i = 0
    
    upper_count = 0
    lower_count = 0
    while i <=3 :
        if phrase.isupper():
            upper_count += 1
        elif phrase.islower():
            lower_count += 1
        i += 1
    
    if upper_count >= 2 :
        maj_phrase = phrase.upper()
        print(maj_phrase)
    else :
        print(phrase)
 
phrase = input("Entrez une valeur :")       
print(maj(phrase))