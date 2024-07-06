def add(a,b):
    return a+b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operación")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingrese su opción (1,2,3,4,5): ")

        if option == "5":
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La suma es:", add(num1, num2))
            elif option == "2":
                print("La resta es:", substract(num1, num2))
            elif option == "3":
                print("La división es:", divide(num1, num2))
            elif option == "4":
                print("La multiplicación es:", multiply(num1, num2))
        
        else:
            print("Opción no válida, por intenta de nuevo")

calculator()        