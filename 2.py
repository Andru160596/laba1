try:
    choker = False
    array = input().split()
    for i in range(len(array)):
        array[i] = int(array[i])
except (ValueError, TypeError):
    print('Дядя, тут шутки не прокатят. Стоит проверочка! Запускай снова')
    raise SystemExit

sum = 0

for i in range(len(array)-1):
    if array[i+1]>array[i]:
       sum = sum + 1 
       choker = True
    else: 
        print('Вы слабое звено. ПРОЩАЙТЕ')
        raise SystemExit
if choker == True:
    print('Вам сегодня повезло')