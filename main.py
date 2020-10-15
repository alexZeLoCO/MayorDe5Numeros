n = float (input ("Introduzca un número: "))        #SOLICITAR VALOR
maximo = n      #VALOR  MÁXIMO = VALOR INTRODUCIDO (EL PRIMERO SIEMPRE ES MÁXIMO)
for i in range (4):     #REPETIR 4 VECES
    i=i+1       #AUMENTAR VALOR DE I EN UNO
    n= float (input ("Introduzca un número: "))     #SOLICITAR NÚMERO
    if (n > maximo):        #CONDICIÓN: SI NÚMERO ES MAYOR A MÁXIMO
        maximo = n      #ACTUALIZAR MÁXIMO

print ("El mayor número de los introducidos es",maximo)     #OUTPUT
