def sum_numbers(variable):
    res = 0
    while variable != 0:
        res += variable % 10
        variable //= 10
    return res

numbers_cube = []
for i in range(1, 1001, 2):
    numbers_cube.append(i ** 3)

numbers_digits = list(map(sum_numbers, numbers_cube))

sum_one = []
for i in range(len(numbers_cube)):
    if numbers_digits[i] % 7 == 0:
        sum_one.append(numbers_cube[i])
rev3 = sum(sum_one)
print(rev3)

#второе задание (b) не смог, требуется объяснение как сделать, спасибо.




