class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.subjects = {}  # Diccionario para almacenar materias y calificaciones

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def calculate_average(self):
        if not self.subjects:
            return 0  # Si no hay materias, el promedio es 0
        total_grades = sum(self.subjects.values())
        return total_grades / len(self.subjects)

    def classify_performance(self):
        average = self.calculate_average()
        if average >= 90:
            return "Excelente"
        elif average >= 75:
            return "Bueno"
        elif average >= 60:
            return "Regular"
        else:
            return "Insuficiente"

    def __str__(self):
        return f"Estudiante: {self.name}, ID: {self.student_id}, Promedio: {self.calculate_average():.2f}, Rendimiento: {self.classify_performance()}"

class ManagementSystem:
    def __init__(self):
        self.students = []  # Lista para almacenar objetos Student

    def register_student(self, student):
        self.students.append(student)

    def show_students(self):
        for student in self.students:
            print(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"Estudiante {student_id} eliminado con éxito.")
        else:
            print(f"Estudiante con ID {student_id} no encontrado.")

if __name__ == "__main__":
    system = ManagementSystem()

    while True:
        print("\n--- Sistema de Gestión de Estudiantes ---")
        print("1. Registrar nuevo estudiante")
        print("2. Agregar materia y calificación")
        print("3. Mostrar todos los estudiantes")
        print("4. Buscar estudiante por ID")
        print("5. Eliminar estudiante por ID")
        print("6. Salir")

        option = input("Selecciona una opción (1-6): ")

        if option == '1':
            name = input("Nombre del estudiante: ")
            student_id = input("ID del estudiante: ")
            student = Student(name, student_id)
            system.register_student(student)
            print(f"Estudiante {name} registrado con éxito.")

        elif option == '2':
            student_id = input("ID del estudiante: ")
            student = system.find_student(student_id)
            if student:
                subject = input("Nombre de la materia: ")
                grade = float(input("Calificación: "))
                student.add_subject(subject, grade)
                print(f"Materia {subject} con calificación {grade} agregada a {student.name}.")
            else:
                print(f"Estudiante con ID {student_id} no encontrado.")

        elif option == '3':
            system.show_students()

        elif option == '4':
            student_id = input("ID del estudiante: ")
            student = system.find_student(student_id)
            if student:
                print(student)
            else:
                print(f"Estudiante con ID {student_id} no encontrado.")

        elif option == '5':
            student_id = input("ID del estudiante: ")
            system.delete_student(student_id)

        elif option == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
