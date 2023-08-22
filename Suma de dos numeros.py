#Primero se piden los números al usuario
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un número: "))

#Se suman los dos números
suma = num1 + num2

#Me gusta usar {} para ingresar los datos
msj_fin = "La suma de {num1} y {num2} es: {suma}"

#Se cambia el formato para imprimir el resultado
print(msj_fin.format(num1=num1, num2=num2, suma=suma))