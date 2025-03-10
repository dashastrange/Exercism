def is_pangram(sentence):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letters_sentence = []
    identificator = []
    x = 0

    for l in sentence.lower():
        if l in alphabet:
            letters_sentence.append(l)
    #print(letters_sentence)
    
    while x in range(len(alphabet)):
        if alphabet[x] in letters_sentence:
            x += 1
            identificator.append('+')
            continue
        #print(identificator)
    
        if alphabet[x] not in letters_sentence:
            x += 1 
            identificator.append('-')
            continue
        #print(identificator)

    if '-' in identificator:
        #print('False')
        return False
    else:
        #print('True')
        return True
        
#is_pangram("abcdefghijklmnopqrstuvwxy")
#is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog")
