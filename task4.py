product_prise = [10, 23, 56, 56.80, 89.90, 78, 67, 32, 56.70]
print(id(product_prise))


def print_prise(lst):
    for i in range(len(lst)):
        rub = int(lst[i])
        cop = round(100 * (lst[i] % 1))
        if i == len(product_prise) - 1:
            print(rub, 'руб', f'{cop:02}', 'коп')
        else:
            print(rub, 'руб', f'{cop:02}', 'коп', end=', ')


print_prise(product_prise)
print(id(product_prise))

product_prise.sort()
print_prise(product_prise)
print(id(product_prise))

revers_prise = sorted(product_prise, reverse=True)
print_prise(product_prise[-5:])

