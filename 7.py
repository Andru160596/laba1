List = ['vk.com','www.google','www.monster.com','odnoklasniki','joycasino']
#List = [c for c in List]
print (List) 
print('')

for i in range(len(List)):
    temp = List[i]
    if temp[:4] != ('www.') and (temp[:8] != ('https://') or temp[:7] != ('http://')):
        List[i] = 'www.' + List[i]
    if temp[:8] != ('https://'):
            List[i] = 'https://' + List[i]
            if not List[i].endswith('.com'):
                List[i] =List[i] + '.com'
print(List)