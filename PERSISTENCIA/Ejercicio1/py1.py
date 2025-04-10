import json
import os

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "salario": self.salario
        }

class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.crearArchivo()

    def crearArchivo(self):
        if not os.path.isfile(self.nomA):
            with open(self.nomA, 'w') as f:
                json.dump([], f)

    def guardarEmpleado(self, e: Empleado):
        with open(self.nomA, 'r+') as f:
            empleados = json.load(f)
            empleados.append(e.to_dict())
            f.seek(0)
            json.dump(empleados, f)

    def buscaEmpleado(self, nombre: str) -> Empleado:
        with open(self.nomA, 'r') as f:
            empleados = json.load(f)
            for emp in empleados:
                if emp["nombre"] == nombre:
                    return Empleado(emp["nombre"], emp["edad"], emp["salario"])
        return None

    def mayorSalario(self, sueldo: float) -> Empleado:
        with open(self.nomA, 'r') as f:
            empleados = json.load(f)
            for emp in empleados:
                if emp["salario"] > sueldo:
                    return Empleado(emp["nombre"], emp["edad"], emp["salario"])
        return None

if __name__ == "__main__":
    archivo = ArchivoEmpleado("empleados.json")
    
    archivo.guardarEmpleado(Empleado("Luis", 28, 2500))
    archivo.guardarEmpleado(Empleado("Andrea", 25, 2000))

    empleado = archivo.buscaEmpleado("Luis")
    if empleado:
        print(f"Empleado encontrado: {empleado.nombre}, Edad: {empleado.edad}, Salario: {empleado.salario}")
    else:
        print("Empleado no encontrado.")

    empleado_mayor_salario = archivo.mayorSalario(3500.0)
    if empleado_mayor_salario:
        print(f"Empleado con mayor salario: {empleado_mayor_salario.nombre}, Salario: {empleado_mayor_salario.salario}")
    else:
        print("No hay empleados con un salario mayor al establecido.")
