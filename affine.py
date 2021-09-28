def inverse(a):
    for x in range(26):
        if a * x % 26 == 1:
            return x


def encrypt(text, key):  # formula (a * x + b) mod N
    N = 26
    a, b = key

    def func(char):
        if char == ' ':
            return char

        if char.islower():
            x = ord(char) - 97
            return chr((a * x + b) % N + 97)
        else:
            x = ord(char) - 65
            return chr((a * x + b) % N + 65)

    return ''.join(map(func, text))


def decrypt(text, key):  # formula a_inverse * (y - b) mod N
    N = 26
    a, b = key

    def func(char):
        if char == ' ':
            return char

        if char.islower():
            y = ord(char) - 97
            return chr(inverse(a) * (y - b) % N + 97)
        else:
            y = ord(char) - 65
            return chr(inverse(a) * (y - b) % N + 65)

    return ''.join(map(func, text))
