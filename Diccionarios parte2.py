#Parte 2 de introducción a diccionarios

equipo = {1:"Harry Styles",2:"Louis Tomlinson",3:"Niall Horan",4:"Liam",5:"Zayn Malik"}

#Buscar a alguien en específico
print(equipo[1])

#Si no existe alguien lanzar un mensaje
print(equipo.get(18,"No existe ese artista"))

#Para saber si está dentro del diccionario
print(4 in equipo)

#Solo mostrar las claves
print(equipo.keys())

#Mostrar solo los valores
print(equipo.values())

#Cuántos hay
print(len(equipo))

#Carolina EM