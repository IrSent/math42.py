"""Let's find out what words have number 42 inside of them."""

letters = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4,
    'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12,
    'm': 13, 'n': 14, 'o': 15, 'p': 16,
    'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24,
    'y': 25, 'z': 26
}

fortytwo = []
with open('words.txt', 'r') as dictionary:
    for word in dictionary.read().split('\n'):
        if word.isalpha():
            value = sum([letters[x] for x in word])
            if value == 42:
                fortytwo.append(word)

with open('fortytwo.txt', 'w') as result:
    result.write("\n".join(fortytwo))
