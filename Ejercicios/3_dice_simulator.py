import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

class DiceSimulator:
    def __init__(self, die):
        self.die = die
        self.results = []

    def simulate_rolls(self, num_rolls):
        self.results = [self.die.roll() for _ in range(num_rolls)]

    def calculate_average(self):
        if not self.results:
            return 0
        return sum(self.results) / len(self.results)

    def calculate_frequencies(self):
        frequencies = {}
        for result in self.results:
            if result in frequencies:
                frequencies[result] += 1
            else:
                frequencies[result] = 1
        return frequencies

    def show_statistics(self):
        if not self.results:
            print("No se han realizado lanzamientos.")
            return
        
        average = self.calculate_average()
        frequencies = self.calculate_frequencies()

        print(f"\nEstadísticas después de {len(self.results)} lanzamientos:")
        print(f"Promedio de los resultados: {average:.2f}")
        print("Frecuencia de cada cara:")
        for side, frequency in frequencies.items():
            print(f"Cara {side}: {frequency} veces")

if __name__ == "__main__":
    # Crear un dado de 6 caras
    die = Die()

    # Crear un simulador de dados
    simulator = DiceSimulator(die)

    while True:
        print("\n--- Simulación de Lanzamiento de Dados ---")
        num_rolls = int(input("¿Cuántos lanzamientos quieres simular? (0 para salir): "))

        if num_rolls == 0:
            print("Saliendo de la simulación...")
            break

        simulator.simulate_rolls(num_rolls)
        simulator.show_statistics()