import random 
import itertools 
import time
from datetime import datetime, timedelta
#https://pythonworld.ru/moduli/modul-datetime.html

f = open('text.txt', 'r')
TeamList = [line.strip() for line in f]
#Список команд в файле

random.shuffle(TeamList) #Рандомим список
TeamList = [TeamList[d:d+4] for d in range(0, len(TeamList), 4)] #Делим команды на 4 группы по 4 команды

print ('\n--Таблица групп:----------------------')
print ('Группа A: ',TeamList[0])
print ('Группа B: ',TeamList[1])
print ('Группа C: ',TeamList[2])
print ('Группа D: ',TeamList[3])
print ('\n--Рассписание матчей:------------------')

#Дата начала
tempDate = "14.09.2017"
#startDate = datetime.datetime.strptime(tempDate, "%d.%m.%Y")
startTime = [14,9,2017]
endTime = [14,4,2018]

print ('Начало сезона', str(startTime[0])+'/'+str(startTime[1])+'/'+str(startTime[2])+' '+ str('22:45') )
print ('Конец сезона', str(endTime[0])+'/'+str(endTime[1])+'/'+str(endTime[2])+' '+ str('22:45') )

now_date = datetime.now()
now_date = now_date.replace(2017,9,14)
print ('\n')

#Расписуем дни
t = open('text_rasp.txt', 'r+') # расписание матчей
a = datetime(2017, 9, 20) #Начало
b = timedelta(days=7) #timedelta - разница между двумя моментами времени, с точностью до микросекунд.... Грубо говоря шаг
while a<=datetime(2018, 4, 14):
    a=a+b
    t.write('%s/%s/%s' % (a.day, a.month, a.year) + '   22:45\n')

f.close()
t.close()