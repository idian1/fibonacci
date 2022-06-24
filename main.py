n = int(input("ingrese la cantidad de numeros de la cadena requeridos "))
a = 0
b = 1
c = 0

if n == 0:
    print("0")
elif n == 1:
    print("0\n1")
else:
    print("0\n1")
    while c <= n-2:
        total = a + b
        a = b
        b = total
        print(total)
        c += 1

# Al ser la secuencia de fibonacci la suma de los 2 numeros anteriores, lo defini como una suma de a + b donde al
# terminar la suma, reemplaza "a" por el numero de "b" y "b" es reemplazado por el total de la suma,
# repitiendose esto n-2 veces.
# esto por que la primera suma se genera con a = 0 y b = 1 lo que hace que la cadena comience desde el segundo 1
# de la secuencia a la cual le faltarian los primeros 2 digitos "0" y "1"
# Para solucionarlo defini que si el numero ingresado por el usuario es 0 mostrara como resultado el
# primer numero de la cadena "0" y si se ingresa el numero "1" se muestran los numeros "0" y "1"
# en el caso de que el numero ingresado sea mayor a "1" la terminal imprimira "0" y "1" seguido de "n-2" digitos lo que
# representara la cantidad de digitos requeridos de la cadena.
# En un principio habia hecho el codigo con un ciclo for, pero me parecio que se veia mas ordenado con un while por eso
# termine escribiendo asi el codigo.
