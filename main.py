import reverse_cypher as rv
import caesar_cypher as ca

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
    