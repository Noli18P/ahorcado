#Crear una clase llamada producto con los siguientes atributos
# codigo, nombre, precio
# Crear su constructor, getter y setter y un método llamado calcular_total al que le pasaremos unas unidades 
#y debe calcular el precio final

class producto:
	def __init__(self, codigo, nombre, precio):
		self.codigo = codigo
		self.nombre = nombre
		self.precio = precio