def is_valid(isbn):
    num_list = []
    numbers = '0123456789'
    isbn_list = list(isbn.replace('-',''))

    print(isbn_list)

    for num in isbn_list:
        if num in numbers:
            num_list.append(num)
        else:
            num_list.append(10)
    print(num_list)

    a, b, c, d, e, f, g, h, i, j = num_list
    print(a, b, c, d, e, f, g, h, i, j)


    
    

is_valid("3-598-21507-X")
    
