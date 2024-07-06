numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"nombre": "Carla",
               "Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29}
print(information)
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
#print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Carla": {"Apellido": "Florida",
               "Altura": 1.60,
               "Edad": 29},
                "Diego": {"Apellido": "Antezana",
               "Altura": 1.80,
               "Edad": 32}}
print(contacts["Carla"])