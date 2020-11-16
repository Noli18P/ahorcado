#Crear una clase llamada producto con los siguientes atributos
# codigo, nombre, precio
# Crear su constructor, getter y setter y un método llamado calcular_total al que le pasaremos unas unidades 
#y debe calcular el precio final

class producto:
	def __init__(self, codigo, nombre, precio):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__precio = precio

	#Getter
	@property
	def codigo(self):
		return self.__codigo

	@property
	def nombre(self):
		return self.__nombre
	
	@property
	def precio(self):
		return self.__precio
	
	#Setter
	@codigo.setter
	def codigo(self, valor):
		self.__codigo = valor

	@nombre.setter
	def nombre(self,valor):
		self.__nombre = valor

	@precio.setter
	def precio(self,valor):
		self.__precio = valor

	#To string
	def __str__(self):
		return 'Codigo: ' + str(self.__codigo) + ' Nombre: ' + str(self.__nombre) + ' Precio: ' + str(self.__precio)  

	#Metodo
	def calcular_total(self, unidades):
		total = self.precio * unidades

		return total
p1 = producto(1, 'Producto 1', 5)
print(p1.calcular_total(5))