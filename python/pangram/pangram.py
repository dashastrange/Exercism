def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_sentence = set()

    for char in sentence.lower():
        if char in alphabet:
            letters_sentence.add(char)
    return len(letters_sentence) == len(alphabet)
