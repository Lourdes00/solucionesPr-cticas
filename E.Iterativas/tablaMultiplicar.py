''' Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10
5.1 Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
5.2 Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone.'''

#Solicitar al usuario que ingrese un número entre 1 y 10
numero = int(input("Ingrese el número para generar la tabla (entre 1 y 10): "))

#Verificar que el número esté en el rango correcto
if 1 <= numero <= 10:
    i = 1  # Inicializar el contador
    print(f"Tabla de multiplicar del {numero}:")
    # Generar la tabla de multiplicar usando un bucle while
    while i <= 10:
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        i += 1  #Incrementar el contador


# Solicitar al usuario que ingrese un número entre 1 y 10
numero = int(input("Ingrese el número para generar la tabla (entre 1 y 10): "))

# Verificar que el número esté en el rango correcto
if 1 <= numero <= 10:
    print(f"Tabla de multiplicar del {numero}:")
    # Generar la tabla de multiplicar usando un bucle for
    for i in range(1, 10):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")