variable = input("Enter variable name in camel case: ")
variable_char_list = list(variable)
snake_case_list = []
char_position = 0

for char in variable_char_list:
    snake_case_list.append(char)
    char_position += 1

    if char.isupper():
        char_position +=1
        snake_case_list.insert(char_position - 2, "_")

else:
    pass

snake_case = ''.join(snake_case_list).lower()
print(snake_case)

