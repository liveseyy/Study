import random as r


def is_valid(m, n):
    try:
        if 0 < int(m) < int(n)+1:
            return True
        else:
            return False
    except ValueError:
        return False


attempts = 0
mes = 'Y'

while mes == 'Y':
    if attempts == 0:
        n = input('Крайняя граница случайного число от 1 до : ')
        z = r.randint(1, int(n))
    m = input(f'Введите число от 1 до {n} включительно: ')
    attempts += 1
    if is_valid(m, n):
        m = int(m)
        if m < z:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif m > z:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', str(attempts))
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...\n')
            mes = input('Хотите попробовать ещё?(Y/N): ')
            attempts = 0

    else:
        print(f'А может быть все-таки введем целое число от 1 до {n}?')
