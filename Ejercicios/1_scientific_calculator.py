import math

class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: División por cero no permitida."

    def power(self, base, exponent):
        return math.pow(base, exponent)

    def square_root(self, num):
        if num < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        return math.sqrt(num)

    def logarithm(self, num):
        if num <= 0:
            return "Error: El logaritmo de un número menor o igual a cero no está definido."
        return math.log(num)

    def sine(self, angle):
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        return math.cos(math.radians(angle))

    def menu(self):
        while True:
            print("\n--- Calculadora Científica ---")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicación")
            print("4. División")
            print("5. Potencia")
            print("6. Raíz Cuadrada")
            print("7. Logaritmo")
            print("8. Seno")
            print("9. Coseno")
            print("10. Salir")

            option = input("Selecciona una operación (1-10): ")

            if option == '10':
                print("Saliendo de la calculadora...")
                break

            if option in ['1', '2', '3', '4', '5']:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                if option == '1':
                    print(f"Resultado: {self.add(num1, num2)}")
                elif option == '2':
                    print(f"Resultado: {self.subtract(num1, num2)}")
                elif option == '3':
                    print(f"Resultado: {self.multiply(num1, num2)}")
                elif option == '4':
                    print(f"Resultado: {self.divide(num1, num2)}")
                elif option == '5':
                    print(f"Resultado: {self.power(num1, num2)}")
            elif option in ['6', '7', '8', '9']:
                num = float(input("Ingresa el número: "))
                if option == '6':
                    print(f"Resultado: {self.square_root(num)}")
                elif option == '7':
                    print(f"Resultado: {self.logarithm(num)}")
                elif option == '8':
                    print(f"Resultado: {self.sine(num)}")
                elif option == '9':
                    print(f"Resultado: {self.cosine(num)}")
            else:
                print("Opción no válida. Por favor, selecciona una opción del 1 al 10.")

if __name__ == "__main__":
    calc = Calculator()
    calc.menu()
