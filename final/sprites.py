# -*- coding: utf-8 -*-

import random
import math

from general import *

def recortar(archivo, ancho_corte, alto_corte):
	matriz = []
	imagen = pygame.image.load(archivo) #.convert()
	imagen_ancho, imagen_alto = imagen.get_size()
	print imagen_ancho, ' ', imagen_alto
	for x in range(0, imagen_ancho/ancho_corte):
		linea = []
		for y in range(0, imagen_alto / alto_corte):
			cuadro = (x*ancho_corte, y*alto_corte, ancho_corte, alto_corte)
			linea.append(imagen.subsurface(cuadro))
		matriz.append	(linea)
	return matriz

def distanciaDosPuntos(a,b):
	nuevoVector = vector(a,b)
	return normaVector(nuevoVector)

def vector(a,b):
	return (b[0]-a[0],b[1]-a[1])    #hace el vector entre 2 puntos

def normaVector(a):
    return math.sqrt(a[0]**2 + a[1]**2)

# ------------------------------------------------------------------
# Calse jugador
# ------------------------------------------------------------------

class Jugador(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# Esta clase define todos los aspectos básicos del personaje principal.
	# Se crean los movimientos, las acciones del jugador y como interactúa
	# con los demás elementos del juego
	# ------------------------------------------------------------------

	juanPerez = recortar('img/juanperez.png', 46, 49)

	# ------------------------------------------------------------------
	# Se definen las listas de choques con los enemigos
	# ------------------------------------------------------------------

	colisionChasqueador = None
	colisionBulimicos = None
	colisionMuercielago = None
	colisionCalaverico = None
	colisionEmpanadas = None

	listaEnemigos = None
	listaModificadores = None
	listaJefes = None

	# modificador 2
	# modificador 3

	# ------------------------------------------------------------------
	# Constructor
	# ------------------------------------------------------------------
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = self.juanPerez[0][0].convert_alpha()
		self.rect = self.image.get_rect()
		self.vida = 1000
		self.var_x = 0
		self.var_y = ALTO
		self.rect.x = ANCHO/2
		self.rect.y = 300
		self.contador = 0  # hace el cambio de imagen para darle movimiento
		self.direccion = 1  # define la direccion de la imagen

	# ------------------------------------------------------------------
	# Interacciones del jugador con el ambiente del juego
	# ------------------------------------------------------------------

	def gravedad(self):

		if self.var_y == 0:
			self.var_y = 1
		else:
			self.var_y += .35

		if self.rect.y >= ALTO - self.rect.height:
			self.rect.bottom = ALTO
			self.var_y = 0

	def update(self):

		self.gravedad()
		self.rect.x += self.var_x

		# ------------------------------------------------------------------
		# Control de elementos básicos del jugador
		# ------------------------------------------------------------------

		# Aquí se hace el cambio de posición del la imagen del sprite para dar movimiento
		if self.contador < 2:
			self.contador += 1
		else:
			self.contador = 0

		# Se verifica que el jugador no supere la pantalla por el lado izquierdo
		if self.rect.right > ANCHO - 100:
			self.rect.right = ANCHO - 100
			self.variacion_x = 0

		# Se verifica que el jugador no supere la pantalla por el lado derecho
		if self.rect.left < 100:
			self.rect.left = 100
			self.variacion_x = 0

		self.rect.y += self.var_y

		if self.direccion == 0:
			self.image = self.juanPerez[self.direccion][0 + self.contador]
		if self.direccion == 1:
			self.image = self.juanPerez[self.direccion][0 + self.contador]


	# ------------------------------------------------------------------
	# Movimientos del jugador y como interactúa con el ambiente de juego
	# ------------------------------------------------------------------

	def moverseIzquierda(self):
		self.var_x = -5
		self.direccion = 0

	def moverseDerecha(self):
		self.var_x = 5
		self.direccion = 1

	def saltar(self):
		self.var_y = -5
		self.rect.y += -2
		self.direccion = 2

	def detenerse(self):
		self.var_x = 0
		self.var_y = 0
		self.direccion = 1

	def disparar(self,balas, todos, direccion):
		bala = Bala()
		bala.direccion = direccion
		bala.rect.x = self.rect.x
		bala.rect.y = self.rect.y
		balas.add(bala)
		todos.add(bala)
		bala.update()

	def quitarVida(self, damage):
		self.vida = self.vida - damage

	def aumentarVida(self, vida):

		if self.vida > 100:
			self.vidaEnemigo = 100
		else:
			self.vida = self.vida + vida



class Enemigo(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# Esta clase define todos los aspectos básicos de los enemigos.
	# Se crean los movimientos, las acciones de los enemigos y como interactúan
	# con los demás elementos del juego
	# ----------------------------------------------------------------

	zombieMordedor = recortar('img/chasqueador.png', 46, 49)
	zombieBulimico = recortar('img/aguita.png', 59, 56)
	muercielago = recortar('img/murcielago.png', 32, 32)
	calaverico = recortar('img/calavericos.png',83,85)
	drSalvador = recortar('img/boss1.png', 63, 75)
	pyramidHead = recortar('img/boss2.png',120,181)
	player=None

	def __init__(self, tipoEnemigo, vidaEnemigo, enemyDamage):

		# inicializo la clase sprite
		# cargo todos los elementos de sprite
		pygame.sprite.Sprite.__init__(self)

		# definimos el tipo de enemigo que se vaya a cargar al ser llamado
		if (tipoEnemigo == 1):
			self.image = self.zombieMordedor[0][0].convert_alpha()

		if (tipoEnemigo == 2):
			self.image = self.zombieBulimico[0][0].convert_alpha()

		if (tipoEnemigo == 3):
			self.image = self.muercielago[0][0].convert_alpha()

		if (tipoEnemigo == 4):
			self.image = self.calaverico[0][0].convert_alpha()

		if (tipoEnemigo == 5):
			self.image = self.drSalvador[0][0].convert_alpha()

		if (tipoEnemigo == 6):
			self.image = self.pyramidHead[0][0].convert_alpha()

		self.rect = self.image.get_rect()
		self.vida = vidaEnemigo
		self.damage = enemyDamage
		self.rect.x = 0  
		self.rect.y = 0
		self.tipoEnemigo = tipoEnemigo
		self.variacion_x = 0 
		self.proximidad = False

	# actualiza la posicion en x permitiendo que se mueve el objeto
	# este metodo refleja lo que quiere que haga la clase
	def update(self):

		p = (self.player.rect.x,self.player.rect.y)
		g = (self.rect.x,self.rect.y)

		if distanciaDosPuntos(p,g) <= 50000:
			self.proximidad = True

		if self.proximidad:

			if self.player.rect.x > self.rect.x or self.rect.x <= 0:
				self.variacion_x = 1

			if self.player.rect.x == self.rect.x:
				self.variacion_x=0

			if self.player.rect.x < self.rect.x or self.rect.x >= ANCHO:
				self.variacion_x=-1

		self.rect.x+=self.variacion_x

	def quitarVida(self, damage):
		self.vida = self.vida - damage

class Boss(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# Esta clase define todos los aspectos básicos de los jefes
	# Se crean los movimientos, las acciones de los enemigos y como interactúan
	# con los demás elementos del juego
	# ----------------------------------------------------------------

	drSalvador = recortar('img/boss1.png', 63, 75)
	pyramidHead = recortar('img/boss2.png',120,181)

	player=None

	def __init__(self, tipoJefe, vidaJefe, bossDamage):

		# inicializo la clase sprite
		# cargo todos los elementos de sprite
		pygame.sprite.Sprite.__init__(self)

		# definimos el tipo de enemigo que se vaya a cargar al ser llamado
		if (tipoJefe == 1):
			self.image = self.drSalvador[0][0].convert_alpha()

		if (tipoJefe == 2):
			self.image = self.pyramidHead[0][0].convert_alpha()

		self.rect = self.image.get_rect()
		self.vida = vidaJefe
		self.damage = bossDamage
		self.rect.x = 0  
		self.rect.y = 0
		self.tipoJefe = tipoJefe
		self.variacion_x = 0 
		self.proximidad = False
		# self.efecto = sonidoJefe

	# actualiza la posicion en x permitiendo que se mueve el objeto
	# este metodo refleja lo que quiere que haga la clase
	def update(self):

		# self.efecto.play()

		p = (self.player.rect.x,self.player.rect.y)
		g = (self.rect.x,self.rect.y)

		if distanciaDosPuntos(p,g) <= 500:
			self.proximidad = True

		if self.proximidad:

			if self.player.rect.x > self.rect.x or self.rect.x <= 0:
				self.variacion_x = 2

			if self.player.rect.x == self.rect.x:
				self.variacion_x = 0

			if self.player.rect.x < self.rect.x or self.rect.x >= ANCHO:
				self.variacion_x = -2

		self.rect.x+=self.variacion_x

	def quitarVida(self, damage):
		self.vida = self.vida - damage

class BarraVida(pygame.sprite.Sprite):
	
	def __init__(self, posicion_x, posicion_y, ancho, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([ancho, 10])
		self.color = color
		self.alto = 10
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = posicion_x
		self.rect.y = posicion_y

	def cambiarBarra(self, x):
		if(not x <= 0):
			self.image = pygame.Surface([x, self.alto])
			self.image.fill(self.color)


class Bala(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load('img/Bala.png').convert_alpha()
		self.rect = self.image.get_rect()
		self.damage = 5
		self.rect.x = 0
		self.rect.y = 0
		self.variacion_x = 10
		self.direccion = 1

	def update(self):

		if self.direccion == 0:
			self.rect.x -= self.variacion_x

		else:
			self.rect.x += self.variacion_x


class Modificadores(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# Se cargan los sprites como atributos de la clase
	# ------------------------------------------------------------------

	# Constructor
	def __init__(self, tipoModificador, valorModificador):
		pygame.sprite.Sprite.__init__(self)

		# ------------------------------------------------------------------
		# Cambia el tipo de modificador
		# ---------------------------------------------------------

		if tipoModificador == 1:
			self.image = pygame.image.load('img/empanada.png').convert_alpha()

		if tipoModificador == 2:
			self.image = pygame.image.load('img/lataGaseosa.png').convert_alpha()

		if tipoModificador == 3:
			self.image = pygame.image.load('img/pizza.png').convert_alpha()

		self.rect = self.image.get_rect()
		self.modificarPersonaje = valorModificador
		self.rect.x = 0
		self.rect.y = 0
		self.var_x = random.randrange(0,5)
		self.var_y = 0

	def gravedad(self):

		if self.var_y == 0:
			self.var_y = 1
		else:
			self.var_y += .35

		if self.rect.y >= ALTO - self.rect.height:
			self.rect.bottom = ALTO
			self.var_y = 0

	def update(self):
		self.gravedad()

		if self.rect.y >= ALTO - self.rect.height:
			self.rect.x += 0
		else:
			self.rect.x += self.var_x

		self.rect.y += self.var_y


class Nivel_1(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# En esta clase se defiene los elementos básicos del primer nivel
	# ------------------------------------------------------------------

	# Constructor
	def __init__(self, imagen_nivel):
		pygame.sprite.Sprite.__init__(self)

		self.fondo = pygame.image.load(imagen_nivel)
		self.dimensionesFondo = self.fondo.get_rect()
		self.ventana = self.fondo.subsurface(0, 70, ANCHO, ALTO)
		print "nivel 1"

class Nivel_2(pygame.sprite.Sprite):

	# ------------------------------------------------------------------
	# En esta clase se defiene los elementos básicos del primer nivel
	# ------------------------------------------------------------------

	# Constructor
	def __init__(self, imagen_nivel):
		pygame.sprite.Sprite.__init__(self)

		self.fondo = pygame.image.load(imagen_nivel)
		self.dimensionesFondo = self.fondo.get_rect()
		self.ventana = self.fondo.subsurface(0, 100, ANCHO, ALTO)
		print "nivel 2"

class Bloque(pygame.sprite.Sprite):

	def __init__(self, ancho, alto, ubicacion):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface([ancho, alto])
		self.image.fill(NEGRO)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.ubicacion = ubicacion

	def update(self):
		if self.ubicacion == 0:
			self.rect.x = 0
		else:
			self.rect.x = ANCHO - 10

