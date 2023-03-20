import random

massive=[]

n=int(input("Размерность массива > "))

for k in range(1,n+1):
    massive.append(random.randint(1,9))

print(massive)

x = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(x - massive[0])
index = 0
for i in range(1, n):
        count = abs(x - massive[i])
        if count < min:
            min = count
            index = i
print(f'Число {massive[index]} в массиве наиболее близко по величине к числу {x}')