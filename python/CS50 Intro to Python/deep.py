"""
implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""

user_input = input()

if user_input.lower().__contains__("42") or user_input.lower().__contains__("forty-two") or user_input.lower().__contains__("forty two"):
    print("Yes")
else:
    print("No")