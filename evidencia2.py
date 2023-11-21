class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    @property
    def info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años.")

persona1 = Persona("Juan", 25)

print(persona1.nombre)  
print(persona1.edad)    

print(persona1.info)    

persona1.cumplir_anios()  

print(persona1.edad)    
