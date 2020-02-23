for x in range(100):
    first_number = float(input('Введите первое число\n'))
    second_number = float(input('Введите второе число\n'))
    operation = input('Выберите операцию(+, -, *, **, /, //, %)\n')
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '**':
        print(first_number ** second_number)
    elif operation == '/':
        print(first_number / second_number)
    elif operation == '//':
        print(first_number // second_number)
    elif operation == '%':
        print(first_number % second_number)
