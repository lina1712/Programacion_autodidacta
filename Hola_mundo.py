print("¡Hola, Mundo!")

array = [-4, 3, -9, 0, 4, 1]
positivo=[]
negativo =[]
zero =[]


for i in array :
    if i > 0 :
        positivo.append (i)
    elif i == 0 :
        zero.append (i)
    else:
        i < 0 
        negativo.append (i)

result_1=(len(positivo))/(len(array))
result_2=(len(zero))/(len(array))
result_3=(len(negativo))/(len(array))

print("{:.6f}".format(result_1)+"\n"+"{:.6f}".format(result_2)+"\n"+"{:.6f}".format(result_3))

          
