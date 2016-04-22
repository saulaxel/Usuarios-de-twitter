# Programa para leer un archivo de texto y separar sus contactos  #

lista_subtextos = []
lista_usuarios = []

archivo = open("Texto.txt","r")
contenido = archivo.read()

# print contenido	

while contenido.find("\n\n")>=0:
	contenido = contenido.partition("\n\n")
	lista_subtextos.append(contenido[0])
	contenido = contenido[2]
# Termina el while
lista_subtextos.append(contenido)
numTextos = len(lista_subtextos)

for i in range (1,numTextos):
	texto = lista_subtextos[i-1]
	while texto.find("@")>=0:
		texto = texto.partition("@")
		texto = texto[2].partition(" ")
		lista_usuarios.append(texto[0])
		texto = texto[2]
	#Termina el while
	lista_final = []
	for j in lista_usuarios:
		if j not in lista_final:
			lista_final.append(j)
		# Termina el if
	# Termina el for
	lista_final.sort()
	print "lista "+ str(i) + " es:"
	print lista_final
	lista_usuarios = []
# Termina el for

## Fin del programa ##
