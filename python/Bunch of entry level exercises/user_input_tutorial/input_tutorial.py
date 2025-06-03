name = input('What is your name? ')
distance_input = input('What is your distance? in km')
distance = int(distance_input)
miles = distance * 0.621371

print(f'Hello {name.capitalize()}, you are {distance} kilometers away. In miles it equals to {miles}')