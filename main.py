class Auto:
    cantidadCreados = None
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self. modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca 
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        count = 0
        for x in self.asientos:
            if x != None:
                count +=1
        return count
    def verificarIntegridad(self):
        
        if self.registro == self.motor.registro:
            for x in self.asientos:
                if x != None:
                    if x.registro != self.registro:
                        return ("Las piezas no son originales")
                else:
                    continue
            return ("Auto original")
        else:            
            return ("Las piezas no son originales")


    
class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    
    def cambiarColor (self, color):
        coloresValidos = ["rojo","verde","amarillo","negro","blanco"]
        if color in coloresValidos:
            self.color = color 

class Motor: 
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro (self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo


           



