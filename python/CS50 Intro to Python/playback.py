"""
implement a program in Python that prompts the user for input and then outputs that same input,
replacing each space with ... (i.e., three periods).
"""

speech = input("Say it: ")
print(speech.replace(" ", "..."))