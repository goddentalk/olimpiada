import copy

def zapolnenie():
    global arr
    arr = []
    for i in range(50000):
        a = input()
        if a != '':
            arr.append(a)
        else:
            break

arr_all = []
index = []

print('Олимпиада по МАТЕМАТИКЕ\n')
print('Введите участников и баллы: ')
zapolnenie()
arr_math = set(arr)
arr_math = list(arr_math)

arr_math1 = []
for i in range(0, len(arr_math)):
    arr_math1.append(arr_math[i].split())

for i in range(len(arr_math1)):
    arr_all.append(arr_math1[i])



print('\nОлимпиада по ФИЗИКЕ\n')
print('Введите участников и баллы: ')
zapolnenie()
arr_fyzik = set(arr)
arr_fyzik = list(arr_fyzik)

arr_fyzik1 = []
for i in range(0, len(arr_fyzik)):
    arr_fyzik1.append(arr_fyzik[i].split())

for i in range(len(arr_fyzik1)):
    arr_all.append(arr_fyzik1[i])


print('\nОлимпиада по ЛИТЕРАТУРЕ\n')
print('Введите участников и баллы: ')
zapolnenie()
arr_liter = set(arr)
arr_liter = list(arr_liter)

arr_liter1 = []
for i in range(0, len(arr_liter)):
    arr_liter1.append(arr_liter[i].split())
    
for i in range(len(arr_liter1)):
    arr_all.append(arr_liter1[i])


bal = 0
bal_mx = 0
name = []

for i in range(len(arr_all)):
    bal = int(arr_all[i][2])
    for j in range(i+1, len(arr_all)):
        if (arr_all[i][0] == arr_all[j][0]) and (arr_all[i][1] == arr_all[j][1]):
            bal += int(arr_all[j][2])
        if bal >= bal_mx:
            bal_mx = bal
            name = arr_all[i][0] + ' ' + arr_all[i][1]



arr_all_copy = []
for i in range(len(arr_all)):
    arr_all_copy.append((arr_all[i][0], arr_all[i][1]))


arr_all_copy = set(arr_all_copy)
arr_all_copy = list(arr_all_copy)

for i in range(len(arr_all_copy)):
    index_arr_all_copy = (f'{i+1}_{arr_all_copy[i][0][0]}_{len(arr_all_copy[i][1])},')
    index.append(index_arr_all_copy)


print("Всего участников: ", len(index))
print('Индексы: ', *index)
print('Большее кол-во бaллов: ', name, bal_mx)
