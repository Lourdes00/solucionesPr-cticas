'''Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared. '''

#datos
altura = float(input("Ingrese la altura de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))
costo_por_m2 = float(input("Ingrese el costo por metro cuadrado de pintura: "))

#calcular el área de la pared
area = altura * ancho
    
#calcular el costo total de la mano de obra
costo_total = area * costo_por_m2
    
print(f"El costo total de la mano de obra es: ${costo_total:.2f}")