def encrypt(text, k):
    new_text = list()
    len_text = len(text)
    for i in range(len_text):
        if text[i] == ' ':
            new_text.append(' ')
        elif text[i].isupper():
            new_text.append(chr(((ord(text[i]) + k - 65) % 26) + 65))
        else:
            new_text.append(chr(((ord(text[i]) + k - 97) % 26) + 97))
    new_text = ''.join(new_text)
    return new_text


def decrypt(text, k):
    new_text = list()
    len_text = len(text)
    for i in range(len_text):
        if text[i] == ' ':
            new_text.append(' ')
        elif text[i].isupper():
            new_text.append(chr(((ord(text[i]) - k - 65) % 26) + 65))
        else:
            new_text.append(chr(((ord(text[i]) - k - 97) % 26) + 97))
    new_text = ''.join(new_text)
    return new_text
