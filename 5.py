
text = (str(input('Введите строку: \n'))).split(' ')

#Вводим строку и разбиваем ее пораздельно с помощью split
#Делаем все быстро, не так как в 4ой


for i in range(len(text)):
    if ((text[i])[0]).isupper(): #Проверка на вверхний регистр
        text[i] = text[i].upper() #Преобразование строки к верхнему регистру
print(' '.join(text)) #Сборка строки из списка с разделителем S