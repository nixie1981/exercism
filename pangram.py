def is_pangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u','v', 'w', 'x', 'y', 'z']
    for letter in sentence:
        if letter.lower() in alphabet:
            alphabet.remove(letter.lower())
    return len(alphabet) == 0
