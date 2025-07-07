vowels = ['a', 'o', 'u', 'i', 'e', 'A', 'O', 'U', 'I', 'E']

def main():
    phrase = input("Say something: ")
    print(shorten(phrase))

def shorten(word):
    for char in word:
        if char in vowels:
            word = word.replace(char, '')
        else:
            continue
    return word


if __name__ == "__main__":
    main()