'''Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que
el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
puntos. '''

def calcular_puntos(ganados, empatados, perdidos):
    puntos_ganados = ganados * 3
    puntos_empatados = empatados * 1
    puntos_perdidos = perdidos * 0 

    puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos
    return puntos_totales

#ejemplo de puntos
ganados = 5
empatados = 3
perdidos = 2

puntos = calcular_puntos(ganados, empatados, perdidos)
print(f"El equipo ha acumulado {puntos} puntos.")