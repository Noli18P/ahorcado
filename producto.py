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
	def __nombre(self):
		return self.___nombre
	
	@property
	def __precio(self):
		return self.___precio
	
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

	#Metodo
	def calcular_total(self, unidades):
		total = precio * unidades

		return total