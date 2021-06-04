class Zoologico:
    def __init__(self, nombre_zoologico):
        self.animales=[]
        self.nombre_zoologico=nombre_zoologico
    def añadir(self, animal):
        self.animales.append(animal)
        return self
    def lista_animales(self):      
        print("En", self.nombre_zoologico, "puedes visitar a :")
        for animal in self.animales:
            print(f"* Nombre: {animal.nombre}, es un {animal.__class__.__name__} y tiene {animal.edad} años,\n   tiene una salud de: {animal.salud} y es {animal.felicidad}mil % felíz :)")
        return self

class Animal:
    def __init__(self, nombre, edad, salud, felicidad):
        self.nombre=nombre
        self.edad=edad       
        self.salud=salud
        self.felicidad=felicidad                 
    def informacion(self):
        print(self.nombre, "edad :",self.edad,"salud:",self.salud,"puntos de animo :",self.felicidad)
        return self
    def alimentar(self):
        self.salud+=10
        self.felicidad+=10
        return self
class tigre(Animal):
    def __init__(self, nombre, edad, salud, felicidad):
        super().__init__(nombre, edad, salud, felicidad)
    def informacion(self):
        super().informacion()
        return self
    def alimentar(self):
        super().alimentar()
        return self
class oso(Animal):
    def __init__(self, nombre, edad, salud, felicidad):
        super().__init__(nombre, edad, salud, felicidad)
    def informacion(self):
        super().informacion()
        return self
    def alimentar(self):
        super().alimentar()
        return self
class leon(Animal):
    def __init__(self, nombre, edad, salud, felicidad):
        super().__init__(nombre, edad, salud, felicidad)
    def informacion(self):
        super().informacion()
        return self
    def alimentar(self):
        super().alimentar()
        return self

