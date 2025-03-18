def is_valid(isbn):
    num_list = []
    numbers = '0123456789'
    isbn_list = list(isbn.replace('-',''))
    int_arr = []
    n = 0
    sum = 0

    for num in isbn_list:
        if num in numbers:
            num_list.append(num)
        else:
            num_list.append(10)

    for index in num_list:
        int_arr.append(int(index))

    while n <= len(num_list):
        for number in int_arr:
            sum = number * n
            n += 1
    print(sum)

    if sum % 11 == 0:
        return True
    else:
        return False
    
