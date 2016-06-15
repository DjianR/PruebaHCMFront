def redondoMax(a):
    maxim= a[0]
    maxim_index = -1
    for indice in range(len(a)):
        num = a[indice]
        test=list(map(int, str(num))) #lista de digitos del numero
        if (test[len(test)-1]== 0):
            print str(num)  + " es redondo"
            if(num>maxim): #Indice del digito mayor
                maxim_index = indice
    print maxim_index

a = [10,5,30,18]
redondoMax(a)
