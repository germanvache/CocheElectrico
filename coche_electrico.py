class Coche:  # parent class (superclass) / clase padre
    def __init__(self, marca, modelo, anio):
        '''Inicializamos atributos del coche'''
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.deposito = 0

    def llenar_deposito(self):
        '''Simula el llenado del deposito del coche'''
        self.deposito = 100
        print("El deposito esta a", self.deposito)

class Bateria:
    '''Un intento simple de modelizar una bateria'''
    def __init__(self, tamanio_bateria = 70):
        '''Inicializamos los atributos de la bateria'''
        self.tamanio_bateria = tamanio_bateria

    def describir_bateria(self):
        '''Imprimir el tamanio de la bateria'''
        print("Este coche tiene una bateria de tamanio", self.tamanio_bateria,"-kwh.")


class CocheElectrico(Coche):
    '''Representa aspectos de un coche, especifico para coches elecricos'''
    def __init__(self, marca, modelo, anio):
        '''Inicializar atributos de superclase.
        Despues inicializar atributos especificos del coche electrico'''
        super().__init__(marca, modelo, anio)
        self.bateria = Bateria() # Instancia como atributo

mi_tesla = CocheElectrico("tesla", "modelo s", 2016)
mi_tesla.llenar_deposito()
mi_tesla.bateria.describir_bateria()
