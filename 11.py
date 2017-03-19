#Напишите генератор frange как аналог range() с дробным шагом. Пример вызова:

def frange(start,end,step):
    #Создаем функцию
    #https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html
    
    st = start # создаем копию стартовой переменной
    start = float(start)    #переводим числа в формат float
    end = float(end)        #переводим числа в формат float
    step = float(step)      #переводим числа в формат float
    step = round(step,2)    #округляем до 2х чисал 
    
    adD = []        #Инициализируем Массив
    adD.append(start)   #Заносим первый эллемент в Массив
    end = int((end-start)/step)     #вычисляем колличество шагов
   
    for i in range(st,end): #Заполнение массива
        adD.append(adD[i-1] + step)     #Пишем -1, така как 1ый элемент уже есть
        round(adD[i-1],2) #Снова округление
    return adD
   
for y in frange(1, 5, 0.1):
    print (round(y,2)) #Снова округление)))
