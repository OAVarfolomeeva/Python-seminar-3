import random

massive=[]

n=int(input("Размерность массива > "))

for k in range(1,n+1):
    massive.append(random.randint(1,9))

print(massive)

k=int(input("Введите число > "))

count=0
for i in range(n):
    if int(massive[i]) == k:
        count += 1

print(f"Число встречается в массиве раз {count}")