def number_classifying(n1, n2):
    temp_keys = {'odd_number', 'even_number'}
    if n1 > n2:
        evens = [n for n in range(n2, n1) if n % 2 == 0]
        odds = [n for n in range(n2, n1) if n % 2 != 0]
    else:
        evens = [n for n in range(n1, n2) if n % 2 == 0]
        odds = [n for n in range(n1, n2) if n % 2 != 0]

    number_list = dict.fromkeys(temp_keys)
    number_list['even_number'] = list(evens)
    number_list['odd_number'] = list(odds)

    print(number_list)


n1 = int(input('input the first number'))
n2 = int(input('input the second number'))
number_classifying(n1,n2)