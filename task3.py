for num in range(1, 101):
    word = "процент"
    if (num % 10) == 1 and num != 11:
        print(num, word)
    elif 1 < (num % 10) <= 4:
        if 10 < num <= 14:
            print(num, word + "ов")
        else:
            print(num, word + "а")
    else:
        print(num, word + "ов")
