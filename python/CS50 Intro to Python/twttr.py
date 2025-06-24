vowels = ['a', 'o', 'u', 'i', 'e', 'A', 'O', 'U', 'I', 'E']
phrase = input("Say something: ")

for char in phrase:
    if char in vowels:
        phrase = phrase.replace(char, '')
    else:
        continue

print(phrase)


