# Clase producto

class Producto:
    
    def __init__(self, codigo: str = None, descripcion: str = None, precio: float = None):
        self.codigo = codigo
        self.descripcion = descripcion 
        self.precio = precio


    def mostrar_datos(self):
        if (self.codigo or self.descripcion or self.precio) == None:
            print(f'Debe inicializar los datos de este producto.')
        else:
            print(f'Codigo: {self.codigo}')
            print(f'Descripcion: {self.descripcion}')
            print(f'Precio: {self.precio}')
# Fin de la clase

# Instanciando la clase producto
codigo_ingresado = input('Codigo del producto: ')
descripcion_ingresada = input('Descripcion del producto: ')
precio_ingresado = input('Precio del producto: ')

producto1 = Producto()
producto1.codigo = codigo_ingresado
producto1.descripcion = descripcion_ingresada
producto1.precio = precio_ingresado

producto1.mostrar_datos()

