#imports
import random
import string

print("Use the function password(length,letters,Capital letters, numbers, special characters) to create your password using True or False (except for length)")
print("Use the function select_pass(length,letters,Capital letters, numbers, special characters) to create your custom password using int numbers")

#random password def

def password (length,low_letters,Cap_letters,numbers,special_characters):

    #lowercase letters or not
    if low_letters == True:
        lettre=string.ascii_lowercase

    else:
        lettre=''

    #Uppercase letters or not
    if Cap_letters == True:
          Capital = string.ascii_uppercase
    else:
        Capital=''

    #numbers or not
    if numbers ==True:
        nombre=string.digits
    else:
        nombre=''

    #special characters or not
    if special_characters == True:
        caractères_spéciaux=string.punctuation
    else:
         caractères_spéciaux=''


    #generates password

    characters = lettre + nombre + caractères_spéciaux + Capital

    password = ''.join(random.choice(characters) for i in range(length))
    print("Random password is:", password)


#Selected Random password

def select_pass (length,low_letters,Cap_letters,numbers,special_characters):

    #lowercase letters or not
    if low_letters >= 0:
        lettre=string.ascii_lowercase

    else:
        lettre=''

    #Uppercase letters or not
    if Cap_letters >= 0:
          Capital = string.ascii_uppercase
    else:
        Capital=''

    #numbers or not
    if numbers >=0:
        nombre=string.digits
    else:
        nombre=''

    #special characters or not
    if special_characters >= 0:
        caractères_spéciaux=string.punctuation
    else:
         caractères_spéciaux=''


    #generates password
    if (low_letters+Cap_letters+special_characters+numbers) > length:
        print("You cannot choose more characters than the length of your password !")
    else:

        characters = lettre + nombre + caractères_spéciaux + Capital

        password = ''.join(random.choice(characters) for i in range(length))
        print("Random password is:", password)
