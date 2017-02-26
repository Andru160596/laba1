text = input('Enter a text: ') # Вводим текст

words = text.split() # Заносим текст в другую переменную разделяя его на пробелы СПЛИТИМ
words.sort(key=len, reverse=True) # Сортируем по длинне (len) в обратном порядке (reverse=True)

for word in words:
    if  len(word) > 7:
        print('Слово больше 7: ', end=' ')  
    elif  4 <= len(word) <= 7:
        print('\n Слово от 4 до 7: ', end=' ')  
    elif  len(word) < 4:
        print('\n Слово меньше 4: ', end=' ')
        

    print(word, end=' ')