msg='welcome to Python 101: Strings'

words_list = msg.split()
word_welcome = words_list[0].capitalize()
word_string = words_list[-1].capitalize()
word_ring = word_string[2:6].capitalize()
word_to = words_list[1].capitalize()
ones = words_list[3]
one = ones[0:1]
name = 'Tyler'
name1 = 'TERRY'
welcome_string = one + ' ' + word_welcome + ' ' + word_ring + ' '  + word_to + ' ' + name

print(welcome_string)
print(welcome_string[::-1]) #backwards

print(msg.replace('Python', 'New Language'))
print('Python' in msg)

msg1 = f'{name1.capitalize()} loves {words_list[2]}'
print(msg1)