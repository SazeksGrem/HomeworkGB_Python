def num_translate():
    translator = input("Введите число на английском: ")
    num_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять'
    }
    for key, value in num_dict.items():
        if key == translator:
            print(value)
        if translator not in num_dict:
            print(None)
num_translate()