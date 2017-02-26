def get_frames(signal,size,overlap):

        print ('Step: ')
        step = size * overlap
        print (step)
        i = 0
        while i<len(signal):
            print (signal[i:i+size]) #от 0 до шага, ot шаг+размер
            i = i + int(step)
    
size = 5     #Размерность
signal = [i for i in range(0,1024)] #Сигнал
overlap = 2.0 #Шаг наложения кадра


get_frames(signal,size,overlap)
