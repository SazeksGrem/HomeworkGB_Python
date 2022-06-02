name_lst = ['Мария', 'Олег', 'Петрушка', 'Александр', 'Игнат', 'Ольга', 'Максим']
def thezaurus(*args):
    res = {}
    for name in name_lst:
        key = name[0].capitalize()
        if key not in res:
            res[key] = []
        res[key].append(name)
    return res
print(thezaurus(name_lst))


