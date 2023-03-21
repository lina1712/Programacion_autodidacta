def simpleArraySum(array):#funcion para sumar elementos de una misma lista

    suma_array = sum(array)
    return suma_array


def compareTriplest(a, b):#funcion para comparar tripletas y dar puntaje a la de mayores numeros

    score_a = 0
    score_b = 0

    for i, x in zip(a,b):
        if i > x:
            score_a +=1
        elif i < x:
            score_b +=1
            
     score =(score_a, score_b)
    return(score)


def aVeryBigSum(ar):#funcion para sumar elementos en una misma lista

    suma_array = sum(ar)
    return suma_array


def diagonalDifference(arr):#funcion para encontrar la diferencia de los numeros diagonales de una matriz

    diagonal_1 = []
    diagonal_2 = []
    indice = 0
    new_indice = 0

    for i in range(0,len(arr)):
        if i == indice:
            new_arr = arr[i]
            for x in range(0,len(new_arr)):
                if x == indice:
                   diagonal_1.append(new_arr[x])
        indice = indice +1

    new_list = list(reversed(arr))

    for y in range (0,len(new_list)):
        if y == new_indice:
            two_arr = new_list[y]
            for k in range(0,len(two_arr)):
                if k == new_indice:
                    diagonal_2.append(two_arr[k])
        new_indice = new_indice + 1

    diference = abs(sum(diagonal_1)- sum(diagonal_2))
    return(diference)
    

def plusMinus(arr): #funcion para obtener las proporciones de una lista en positivos, negativos y zero

    size_arr = len(arr)
    positivo = 0
    negativo = 0
    zero = 0

    for i in arr:
        if i > 0:
            positivo = positivo + 1
        elif i < 0:
            negativo = negativo + 1
        else:
            zero = zero + 1

    resul1=(positivo/size_arr)
    resul2=(negativo/size_arr)
    resul3=(zero/size_arr)

    return (print("{:.6f}".format(resul1)+"\n"+"{:.6f}".format(resul2)+"\n"+"{:.6f}".format(resul3)))


#num = 20

#for i in range(num):
 #   print("."*(num -i -1)+"#"*(1*i+1))

#for i in range(num):
 #   print("."*(num -i -1)+"#"*(2*i+1))

#for i in range(int(num/2)):
 #   print("."* int(num - num/4)+"#"* int(num/2))


def staircase(n):

    num = n

    for i in range(num):
        draw = print(" "*(num -i - 1)+"#"*(1*i+1))

    return (draw)


def miniMaxSum(arr):#funcion para devolver la suma de una lista sin el mnimo y sin el maximo

    minimo = min(arr)
    maximo = max(arr)

    suma1_lista=(sum(arr)- minimo)
    suma2_lista=(sum(arr)- maximo)
    

    return(print (f"{suma2_lista} {suma1_lista}"))


def birthdayCakeCandles(candles): # te devuele la cantidad de numeros maximos que hay en una lista
    
    n = len(candles)
    max_candles = max(candles)
    count_candles = 0

    for i in candles:
        if i == max_candles:
            count_candles +=1

    return(count_candles)


def timeConversion(s): # convierte las horas en formato am y pm al formato de 24 horas

    hora = (s[0:2])
    minutos = (s[3:5])
    segundo = (s[6:8])

    for i in s:
        if i == "P":
            hora = int(hora)+12
            if hora == 24 and minutos != "00":
               hora = 12
        elif i == "A":
            if hora == "12":
               hora = "00"

    hora_oficial=(str(hora)+":"+(minutos)+":"+(segundo))
            
    return(hora_oficial)   
        
        


    
    
      
                    
           




    
