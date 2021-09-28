def encrypt(text, key):
    alphabet = sorted(key)
    new_text = list()
    for char in text:
        if char == ' ':
            new_text.append(' ')
        else:
            new_text.append(key[alphabet.index(char)])
    new_text = ''.join(new_text)
    return new_text


def decrypt(text, key):
    alphabet = sorted(key)
    new_text = list()
    for char in text:
        if char == ' ':
            new_text.append(' ')
        else:
            new_text.append(alphabet[key.index(char)])
    new_text = ''.join(new_text)
    return new_text
