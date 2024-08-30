import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['Rojo', 'Azul', 'Verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)