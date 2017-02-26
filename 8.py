import random

number = int(random.uniform(0, 1000))
print(number, " - Рандомное число")
#random.uniform(A, B) - случайное число с плавающей точкой, A ≤ N ≤ B (или B ≤ N ≤ A).


nArray = [random.randrange(0, 1000) for i in range(number)]
print (nArray)
#Цикл наполняющий массив

p = 2 
i = 0
while p**i <= number:
    stepen = p**i
    print('2^',i, '= ',stepen)
    i = i + 1
#Просщет степени

appendix = stepen - number
for i in range(appendix):
    nArray.append(0)
print(nArray)
#Заполнение нулями массива