# - -coding: utf - 8 - 

#Desventajas del lenguaje
#Python es muy "Keysensitive"
#Algunos comandos encontrados por internet, no son validos, porque pertenecen a otro parche de Python
#Aunque presuma de su facilidad, muchas veces es poco intuitivo

#Ventajas del lenguaje
#Gran facilidad de interprestacion de variables (a la hora de crearlas)
#Ahorra codigo


class Dado:
	numDado = 0      #No hace falta ni Set ni Get


	def Tirada (self):	#El dado es tirado
        		
		self.numDado = random.randint(1, 6)		#Se genera un numero del 1 al 6 y se guarda en numDado

	def Comparar (self, n1, M3): #Comparamos las tiradas
#Al ser una funcion dentro de una CLASE, tenemos que utilizar el "SELF" para poder llamar las variables 
#como el "ME." en visual basic.
		self.num1 = n1
		self.num2 = M3
		self.codigo = 0
		if self.num1 > self.num2:
		 	return 1
		elif self.num1 < self.num2:
			return 2
		else:
			return 3


class Jugador:

	tirada  = 0 	#No hace flata ni Set ni Get. 
	contador = 0     # Contador para las tiradas ganadas



import random  #Para poder utilizar el "RANDOM", importamos la clase "random" del sistema

#Creamos objetos para las clases.
dado1 = Dado() 
Jugador1 = Jugador()
Jugador2 = Jugador()


#Introduccion  (No he querido ponerlo en una funcion, porque las variables "NomJugador1" y "NomJugador2")
#me interesa que sean globales.

print """
Este juego se llama TIRA EL DADO.


Solo pueden jugar dos personas, (Jugador1, Jugador2).
Si quieres empezar, introduzca el nombre del Jugador1
 y después el nombre del Jugador2.

Si no quiere jugar, pulse la tecla [1] """

NomJugador1 = raw_input ()  #Pedimos una cadena de caracteres para "Jugador1"
if NomJugador1  == '1':
		exit() #si  es 1, sal del programa.

NomJugador2 = raw_input ()  #"Jugador2"  (Si queremos pedir un numero, tendria que ser "input()")
if NomJugador2 == '1':
		exit()

cnt = 0 #El CNT del While

def Pregunta(nombre):  #preguntar si quiere tirar o rendirse
	nombre1 = nombre
	print """
	%s, si quieres tirar, pulsa [ENTER], 
	Si quiere rendirte pulsa [2]
	""" % (nombre1)

	decision = raw_input ()  
	if decision  == '2':
			exit()

def Mostrar(nombre, num1, nombreX): #Mostrar tirada
	nombre1 = nombre
	num = num1
	nombre2  = nombreX
	print """
	%s has sacado un %r. 
	Ahora le toca ha %s
	""" % (nombre1, num, nombre2)



#Bucle while 10
while cnt <= 10:
	Pregunta (NomJugador1)  #llamamos la funcion Pregunta	

	dado1.Tirada()	#Tiramos el dado
	Jugador1.tirada = dado1.numDado  #Guardamos la tirada del dado en "Jugador1.tirada"

	Mostrar(NomJugador1, Jugador1.tirada, NomJugador2)  #Mostramos la tirada

	Pregunta (NomJugador2) #Preguntamos al segundo jugador

	dado1.Tirada()
	Jugador2.tirada = dado1.numDado

	print """
	%s has sacado un %r. 
	
	""" % (NomJugador2, Jugador2.tirada)


	
#Comparamos la tirada, con los valores de las tiradas

	if dado1.Comparar(Jugador1.tirada, Jugador2.tirada) == 1:

		Jugador1.contador = Jugador1.contador + 1  	#Le sumamos 1 al contador creado en la clase "Jugador"
		print "GANA %s" % (NomJugador1)
	elif dado1.Comparar(Jugador1.tirada, Jugador2.tirada) == 2:

		Jugador2.contador = Jugador2.contador + 1
		print "GANA %s" % (NomJugador2)
	elif dado1.Comparar(Jugador1.tirada, Jugador2.tirada) == 3:

		print "EMPATE "

	print " %s, lleva %r" % (NomJugador1, Jugador1.contador)		#Mostramos los contadores de los dos jugadores
	print " %s, lleva %r" % (NomJugador2, Jugador2.contador)
	tiempo = raw_input()


	cnt += 1   #Le sumamos 1 al CNT del WHILE (loop)


#Fuera del while, cuando ha terminado el bucle


#Utilizo la misma funcion de "Dado" para comprar los contadores de los jugadores y saber quien ha ganado.

if dado1.Comparar(Jugador1.contador, Jugador2.contador) == 1:
	
	print " %s HAS GANADO!!!!! HOO YEA" % (NomJugador1)
elif dado1.Comparar(Jugador1.contador, Jugador2.contador) == 2:
	
	print " %s  HAS GANADO !!!! HOOO YEA" % (NomJugador2)
elif dado1.Comparar(Jugador1.contador, Jugador2.contador) == 3:
	print "EMPATE :S"
