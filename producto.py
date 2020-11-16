#Crear una clase llamada producto con los siguientes atributos
# codigo, nombre, precio
# Crear su constructor, getter y setter y un método llamado calcular_total al que le pasaremos unas unidades 
#y debe calcular el precio final

class producto:
	def __init__(self, codigo, nombre, precio):
		self.__codigo = codigo
		self.__nombre = nombre
		self.__precio = precio

	def calcular_total(self, unidades):
		total = precio * unidades

		return total