def non_empty(funcToDec):
    def wrapper(): #Обертка
        print ('Было')
        print (funcToDec()) #Выводим список как он был
        temp = funcToDec()  #Переносим список в переменную
        
        for index, data in enumerate(temp):  #КОЛДУЕМ И УБЕРАЕМ ЛИШНИЕ ПРОБЕЛЫ
            if data == ' ' or data == '':
                del temp[index]
        print ('Стало') 
        print (temp)
    return wrapper()

@non_empty 
def get_pages():
    return ['chapter1', ' ', 'contents', '', 'line1']