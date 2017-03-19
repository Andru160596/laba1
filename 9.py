def cashInput():
    print ('Сколбко будешь снимать: ')
    return int(input('Введите кеш: '))

bank = {1000:10, 100:100, 50:150, 10:500} #abstract money
print ('Денег в банкомате:')
print ('Купюры - \'1000\', количество -',bank[1000])
print ('Купюры - \'100\', количество -',bank[100])
print ('Купюры - \'50\', количество -',bank[50])
print ('Купюры - \'10\', количество -',bank[10])

normalBank = [10,100,150,500]

out = False

while out == False:
    try:
        cash = 0
        cash = cashInput()
        if cash % 10 != 0:
            raise ValueError
        else:
            out = True
    except ValueError:
        cash = 0
        print ('Ошибочка')
#cash = cashInput()
listCash = list(str(cash))      
#косари 1000
thousands = int(cash/1000)
cashOut = 0
i = 0
while i<thousands:          
    if normalBank[0] != 0:
        cashOut = cashOut + 1000
        normalBank[0] = normalBank[0]-1 
    else:
        print('Ошибочка')
        input()
        raise SystemExit
    i = i + 1

#соточки 100
hundreds = int ((cash-cashOut)/100)
i = 0
while i<hundreds:
    if normalBank[1] != 0:
        cashOut = cashOut + 100
        normalBank[1] = normalBank[1]-1
    else:
        print('Ошибочка')
        input()
        raise SystemExit
    i = i + 1
#полтосики 50
halfs = int((cash-cashOut)/50)
i = 0
while i<halfs:
    if normalBank[2] != 0:
        cashOut = cashOut + 50
        normalBank[2] = normalBank[2]-1
    else:
        print('Ошибочка')
        input()
        raise SystemExit
    i = i + 1
#Червонцы 10
tens = int((cash-cashOut)/10)
i = 0
while i<tens:
    if normalBank[3] != 0:
        cashOut = cashOut + 10
        normalBank[3] = normalBank[3]-1
    else:
        print('Ошибочка')
        input()
    i = i + 1

print(cashOut)
print('Осталось денег(1000/100/50/10)  :   ',normalBank)
