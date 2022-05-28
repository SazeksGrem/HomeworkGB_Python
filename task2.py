my_time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_time))
i = 0
while i < len(my_time):
    if my_time[i].isdigit():
        my_time[i] = my_time[i].zfill(2)
    elif my_time[i].startswith('+'):
        my_time[i] = my_time[i].zfill(3)
    i += 1
n = 1
while n < len(my_time):
    if my_time[n].isdigit() or my_time[n].startswith('+') and my_time[n][1:].isdigit():
        my_time.insert(n, '"')
        my_time.insert(n + 2, '"')
        n += 1
    n += 1

print(my_time)
print(id(my_time))

stl = ""
for n in my_time:
    if n.isalpha():
        stl += ''.join(f'{" "}{str(n)}{" "}')
    else:
        stl += ''.join(str(n))
stl = stl.strip()
print(stl)

