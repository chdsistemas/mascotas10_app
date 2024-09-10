class Servicio:
    def __init__(self,
                 codigo: str = None,
                 nombre: str = None,
                 precio: float = None
                 ):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def imprimir_datos(self):
        if (self.get_codigo() is None or self.get_nombre() is None or self.get_precio() is None):
            print('Debe inicializar todos los datos...')
        else:    
            print(f'Codigo: {self.get_codigo()}')
            print(f'Nombre: {self.get_nombre()}')
            print(f'Precio: {self.get_precio()}')
    

    def get_codigo(self):
        return self.codigo

    
    def set_codigo(self):
        codigo_ingresado = input('Código del servicio: ')
        self.codigo = codigo_ingresado

    
    def get_nombre(self):
        return self.nombre
    

    def set_nombre(self):
        nombre_ingresado = input('Nombre del servicio: ')
        self.nombre = nombre_ingresado


    def get_precio(self):
        return self.precio
       

    def set_precio(self):
        precio_ingresado = float(input('Precio del servicio: '))
        self.precio = precio_ingresado


# Fin de la clase

# Creando instancias de servicios

servicio1 = Servicio()
servicio1.set_codigo()
servicio1.set_nombre()
servicio1.set_precio()

servicio1.imprimir_datos()

