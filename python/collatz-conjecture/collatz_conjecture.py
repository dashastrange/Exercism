def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    steps = 0
    while number != 1:
         steps += 1
         if number % 2 == 0:  # if the number is even
             number /= 2
         else:  # other case
             number = number * 3 + 1
            
    return steps
