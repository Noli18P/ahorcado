class persona():
	def __init__(self,edad,estatura):
		self.edad = edad
		self.estatura = estatura

	def printData(self):
		print(f'Edad : {edad} Estatura: {estatura}')

def main():
	edad = int(input('Ingresa tu edad: '))
	estatura = float(input('Ingresa tu estatura: '))
	nombre = input('DIme tu nombre: ')

	nombre = persona(edad,estatura)
	print(nombre.printData)


main()