import random

def encrypt(text, key):
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    new_text = list()
    for char in text:
        try:
            new_text.append(key[alphabet.index(char)])
        except:
            new_text.append(' ')
    new_text = ''.join(new_text)
    return new_text

def decrypt(text, key):
    alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    new_text = list()
    for char in text:
        try:
            new_text.append(alphabet[key.index(char)])
        except:
            new_text.append(' ')
    new_text = ''.join(new_text)
    return new_text
