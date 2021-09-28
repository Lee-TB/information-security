import reverse_cypher as rv
import caesar_cypher as ca
import simple_SC
import random
import affine as af

if __name__=='__main__':
    text = 'Reverse Cypher'
    encrypt = rv.encrypt(text)
    decrypt = rv.decrypt(encrypt)
    print('reverse cypher: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt), end='\n\n')


    text = 'Caesar Cypher'
    encrypt = ca.encrypt(text, 3)
    decrypt = ca.decrypt(encrypt, 3)
    print('caesar cypher: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt), end='\n\n')
    

    key = [chr(i) for i in range(ord('A'), ord('z')+1) if i <= ord('Z') or i >= ord('a')]
    random.seed(1)
    random.shuffle(key)
    text = 'Simple SC'
    encrypt = simple_SC.encrypt(text, key)
    decrypt = simple_SC.decrypt(encrypt, key)
    print('simple SC: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt), end='\n\n')


    text = 'Affine Cypher'
    encrypt = af.encrypt(text, (9, 3))
    decrypt = af.decrypt(encrypt, (9, 3))
    print('Affine cypher: encrypt "{}", decrypt "{}"'.format(encrypt, decrypt), end='\n\n')