import reverse_cypher as rv
import caesar_cypher as ca
import simple_SC
import random

if __name__=='__main__':
    text = 'reverse cypher'
    encrypt = rv.encrypt(text)
    decrypt = rv.decrypt(encrypt)
    print('reverse cypher: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt))
    print()


    text = 'caesar cypher'
    encrypt = ca.encrypt(text, 3)
    decrypt = ca.decrypt(encrypt, 3)
    print('caesar cypher: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt))
    print()
    

    key = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' ')
    random.seed(1)
    random.shuffle(key)
    text = 'ABC D'
    encrypt = simple_SC.encrypt(text, key)
    decrypt = simple_SC.decrypt(encrypt, key)
    print('simple SC: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt))
    print()