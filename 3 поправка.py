import re

cheker = False
while cheker == False:
    try:
        bablo = str(input())
        bablo = re.sub(r'\s', '', bablo)
        bablo = int(bablo)
        if len(str(bablo)) !=16:
            raise ValueError
        cheker = True
    except ValueError:
        print('Ошибка')
   
     
bablo = str(bablo)
print(bablo[:4]+' **** **** '+bablo[12:])