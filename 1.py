try:
    bablo = float(input())
    if bablo<=0:
            raise ValueError
except (ValueError, TypeError):
    print('Введено не число или вы в минусе(((. Запустите программу снова и впреть пытайтеь не оплашать!')
    raise SystemExit
    
RUB = int(bablo)
COP = bablo % 1
COP = round(COP,2) * 100

print('Кеш на руках: %s руб %s коп' %(RUB,int(COP)))