#Mostrar los números desde el 0 al número solicitado al usuario (input)

numero = int (input("Escribir numero:"))

print("Numero del 0 al " , numero)
for i in range (numero + 1):
    print(i)