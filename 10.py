import re
#ВЛЮЧАЕМ РЕГУЛЯРНЫЕ УРАВНЕНИЯ........
#https://tproger.ru/translations/regular-expression-python/

print('Введите пароль. Минимум 6 символа\n')
pswrd = input()
#Вводим пароль
while len(pswrd)<6:
        print('Введите снова пароль')
        pswrd = input()
#Проверочка на символы
        

i = 0
#Счетчик
if re.search(r'[A-Z]', pswrd):
        i=i+1
if re.search(r'[a-z]', pswrd):
        i=i+1
if re.search(r'[0-9]', pswrd):
        i=i+1
                         
lvl = ['Новичок','Любитель','Тяжелый']
print('Ваш пароль:',lvl[i])   
    
    
