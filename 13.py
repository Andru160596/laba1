def extra_enumerate(someArray, start):
    n = start #номер
    cum = 0 #хранится накопленная сумма на момент текущей итерации
    for elem in someArray:   
        yield n, elem  #Генератор http://qualcode.ru/article/python_yield/
        n += 1
        cum = cum + elem
        print(elem,',',cum,',',cum*0.1)


x  = [1,3,4,2] 
for i in extra_enumerate(x,0):
    print() 