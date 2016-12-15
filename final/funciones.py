# -*- coding: utf-8 -*-	

import pygame
import random

from nivel22 import *
from sprites import *
from general import *


def principal_menu():
	fondoprincipal=pygame.image.load("menu2/menuz.jpg")
	pantallaprincipal = pygame.display.set_mode([ANCHO,ALTO])
	pantallaprincipal.fill(NEGRO)
	fuente3=pygame.font.SysFont('monospace',30) 
	fuente=pygame.font.Font('DEMON SKER.ttf', 90)
	valorprincipal=0
	txt_menu=fuente.render("Rise Of Dead", True, BLANCO)
	txt_menu1=fuente3.render("1-Iniciar Juego", True, BLANCO)
	txt_menu2=fuente3.render("2-Instrucciones", True, BLANCO)
	txt_menu4=fuente3.render("0-Cerrar Juego", True, ROJO)
	fin=False
	while not fin:
		if(not pygame.mixer.music.get_busy()):
				pygame.mixer.music.load('menu2/intro.mp3')
				pygame.mixer.music.play()
		tecla=pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1):
						valorprincipal=1
						fin=True
				if (event.key == pygame.K_2):
						valorprincipal=2
						fin=True
				if (event.key == pygame.K_3):
						valorprincipal=3
						fin=True
				if (event.key == pygame.K_0):
						valorprincipal=0
						fin=True
		pantallaprincipal.blit(fondoprincipal, (0,0))
		pantallaprincipal.blit(txt_menu, [50, 150])
		pantallaprincipal.blit(txt_menu1, [50, 320])
		pantallaprincipal.blit(txt_menu2, [50, 350])
		pantallaprincipal.blit(txt_menu4, [50, 380])
		pygame.display.flip()
	return valorprincipal

def Instrucciones():
	fondoinstrucciones=pygame.image.load("menu2/instrucciones.jpg")
	pantallainstrucciones = pygame.display.set_mode([ANCHO,ALTO])
	pantallainstrucciones.fill(NEGRO)
	
	valor=0
	fin=False
	while not fin:
		tecla=pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_0):
						fin = True

		pantallainstrucciones.blit(fondoinstrucciones, (0,0))
		pygame.display.flip()

def main():

	# ------------------------------------------------------------------
	# Configuracion inicial del juego
	# ------------------------------------------------------------------

	pygame.init()
	pantalla = pygame.display.set_mode([ANCHO,ALTO])

	# ------------------------------------------------------------------
	# listas para las colisiones de los sprites
	# ------------------------------------------------------------------

	todos = pygame.sprite.Group()
	principal = pygame.sprite.Group()
	balas = pygame.sprite.Group()
	enemigos = pygame.sprite.Group()
	modificadores = pygame.sprite.Group()
	jefePrimerNivel = pygame.sprite.Group()
	muros = pygame.sprite.Group()
	barraVida = pygame.sprite.Group()

	# ------------------------------------------------------------------
	# Adición de todos los elementos a las listas de colisiones
	# ------------------------------------------------------------------

	juanperez = Jugador() # Personaje principal
	principal.add(juanperez)
	todos.add(juanperez)

	drSalvador = Boss(1, 1000, 5)

	# muros
	bloqueDerecho = Bloque(10,ALTO,0)
	bloqueIzquierdo = Bloque(10,ALTO,1)

	muros.add(bloqueDerecho)
	muros.add(bloqueIzquierdo)
	todos.add(bloqueDerecho)
	todos.add(bloqueIzquierdo)

	# Barra de vida
	vidaJugador = BarraVida(50, 0, juanperez.vida, ROJO)
	barraVida.add(vidaJugador)
	todos.add(vidaJugador)

	# ------------------------------------------------------------------
	# Adicionamos las listas de colisiones con los enemigos
	# ------------------------------------------------------------------

	juanperez.listaModificadores = modificadores
	juanperez.listaEnemigos = enemigos
	juanperez.listaJefes = jefePrimerNivel

	# ------------------------------------------------------------------
	# Variables para el control de enemigos del primer nivel
	# ------------------------------------------------------------------

	contador_chasqueador = 10
	contador_bulimico = 10
	contrador_murcielago = 10
	contador_calavera = 10

	contadorEmpanada = 5
	contadorGaseosa = 3
	contadorPizza = 5

	controlCantidadEnemigos = 5
	controlCantidadModificadores = 5
	controlBossNivel1 = 1

	# ------------------------------------------------------------------
	# Se establece el nivel actual del juego
	# ------------------------------------------------------------------

	# Se define una lista en la que se almacena los diferentes niveles
	niveles =[]
	niveles.append(Nivel_1('img/fondo.jpg'))
	niveles.append(Nivel_2('img/fondo.jpg'))


	# Se agragan los diferentes niveles a la lista de niveles
	posicion_nivel_actual = 0


	# ------------------------------------------------------------------
	# Elementos musicales del juego
	# ------------------------------------------------------------------

	# pygame.mixer.music.set_volume() # Volumen
	efectoDisparo = pygame.mixer.Sound('recursos/musica/pistol.wav')
	efectoMotocierra = pygame.mixer.Sound('recursos/musica/Motosierra_Efecto_de_Sonido_Chainsaw_Sound_Effect.wav')

	# ------------------------------------------------------------------
	# Configuraciones de movimiento de la pantalla
	# ------------------------------------------------------------------

	variacion_x = 0
	posicion_x = 0
	reloj = pygame.time.Clock()
	fin = False

	fondoprincipal=pygame.image.load("menu2/menuz.jpg")
	pantallaprincipal = pygame.display.set_mode([ANCHO,ALTO])
	pantallaprincipal.fill(NEGRO)
	fuente3=pygame.font.SysFont('monospace',30) 
	fuente=pygame.font.Font('DEMON SKER.ttf', 90)
	valorprincipal=0
	txt_menu=fuente.render("Rise Of Dead", True, BLANCO)
	txt_menu1=fuente3.render("1-Iniciar Juego", True, BLANCO)
	txt_menu2=fuente3.render("2-Instrucciones", True, BLANCO)
	txt_menu4=fuente3.render("0-Cerrar Juego", True, ROJO)

	terminar=False

	while not terminar:
		if(not pygame.mixer.music.get_busy()):
				pygame.mixer.music.load('menu2/intro.mp3')
				pygame.mixer.music.play()
		tecla=pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if (event.key == pygame.K_1):
						valorprincipal=1
						terminar=True
				if (event.key == pygame.K_2):
						valorprincipal=2
						Instrucciones()
						terminar=True
				if (event.key == pygame.K_0):
						valorprincipal=1
						terminar=True
						fin = True

		pantallaprincipal.blit(fondoprincipal, (0,0))
		pantallaprincipal.blit(txt_menu, [50, 150])
		pantallaprincipal.blit(txt_menu1, [50, 320])
		pantallaprincipal.blit(txt_menu2, [50, 350])
		pantallaprincipal.blit(txt_menu4, [50, 380])
		pygame.display.flip()

	
	while not fin:

		# ------------------------------------------------------------------
		# las canciones para los niveles
		# ------------------------------------------------------------------

		if not pygame.mixer.music.get_busy():

			if posicion_nivel_actual == 0:
				pygame.mixer.music.load('recursos/musica/nivel1.mp3')
			pygame.mixer.music.play()

		# ------------------------------------------------------------------
		# Lógica del juego
		# ------------------------------------------------------------------

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_LEFT:
					juanperez.moverseIzquierda()

				if event.key == pygame.K_RIGHT:
					juanperez.moverseDerecha()

				if event.key == pygame.K_UP:
					juanperez.saltar()

				if event.key == pygame.K_SPACE:
					juanperez.detenerse()


				if event.key == pygame.K_f:

					if juanperez.direccion == 1:
						juanperez.disparar(balas, todos, 1)
						efectoDisparo.play()
					else:
						juanperez.disparar(balas, todos, 0)
						efectoDisparo.play()




		# ------------------------------------------------------------------
		# Control del jugador para los límites de la pantalla
		# ------------------------------------------------------------------

		if juanperez.rect.right >= ANCHO - 100:
			posicion_x += 5
		if juanperez.rect.left <= 100:
			posicion_x -= 5

		if posicion_x > 0 and posicion_x < (nivel_actual.dimensionesFondo.width - ANCHO):
			nivel_actual.ventana = nivel_actual.fondo.subsurface(posicion_x,70,ANCHO,ALTO)
			print posicion_x

		# ------------------------------------------------------------------
		# Creando enemigos aleatoriamente
		# ------------------------------------------------------------------

		while controlCantidadEnemigos >= 0:
			
			tipoEnemigo = random.randrange(1,5)
			opcionSalida = random.randrange(1,5)

			# ------------------------------------------------------------------
			# Control de creacion de enemigos
			# ------------------------------------------------------------------

			if tipoEnemigo == 1:
				enemigo = Enemigo(tipoEnemigo,300, 5)
				enemigo.player = juanperez
				enemigos.add(enemigo)

			if tipoEnemigo == 2:
				enemigo = Enemigo(tipoEnemigo,270, 5)
				enemigo.player = juanperez
				enemigos.add(enemigo)

			if tipoEnemigo == 3:
				enemigo = Enemigo(tipoEnemigo,100, 5)
				enemigo.player = juanperez
				enemigos.add(enemigo)

			if tipoEnemigo == 4:
				enemigo = Enemigo(tipoEnemigo,300, 5)
				enemigo.player = juanperez
				enemigos.add(enemigo)

			# ------------------------------------------------------------------
			# Control de la salida de los enemigos
			# ------------------------------------------------------------------

			if opcionSalida == 1:
				enemigo.rect.x = random.randrange(-2000, 0)

			if opcionSalida == 2:
				enemigo.rect.x = random.randrange(-2500, -200)

			if opcionSalida == 3:
				enemigo.rect.x = random.randrange(850, 950)

			if opcionSalida == 4:
				enemigo.rect.x = random.randrange(800, 900)

			if tipoEnemigo == 3:
				enemigo.rect.y = 420
			else:
				enemigo.rect.y = ALTO - enemigo.rect.height

			todos.add(enemigo)

			controlCantidadEnemigos -= 1


		# ------------------------------------------------------------------
		# Creando modificadores aleatoriamente
		# ------------------------------------------------------------------

		if len(enemigos) == len(enemigos) / 2:

			while controlCantidadModificadores >= 0:
				
				tipoModificador = random.randrange(1,4)
				opcionSalida = random.randrange(1,5)
				opcionPosicion = random.randrange(-150000, - 5000)


				# ------------------------------------------------------------------
				# Control de creacion de modificadores
				# ------------------------------------------------------------------

				if tipoModificador == 1:
					tiempoModificadores = 1000
					while tiempoModificadores >= 0:
						print "esperando para crear modificadores"
						# pass
						tiempoModificadores -= 1

					modificador = Modificadores(tipoModificador, 5)
					modificadores.add(modificador)
					contadorEmpanada -= 1

				if tipoModificador == 2:
					tiempoModificadores = 5
					while tiempoModificadores >= 0:
						print "esperando para crear modificadores"

						tiempoModificadores -= 1

					modificador = Modificadores(tipoModificador, 5)
					modificadores.add(modificador)
					contadorGaseosa -= 1

				if tipoModificador == 3:
					tiempoModificadores = 5000
					while tiempoModificadores >= 0:
						print "esperando para crear modificadores"
						tiempoModificadores -= 1

					modificador = Modificadores(tipoModificador, 5)
					modificadores.add(modificador)
					contadorPizza -= 1

					# ------------------------------------------------------------------
					# Control de la salida de los modificadores
					# ------------------------------------------------------------------

					if opcionSalida == 1:
						modificador.rect.y = opcionPosicion

					if opcionSalida == 2:
						modificador.rect.y = opcionPosicion

					if opcionSalida == 3:
						modificador.rect.y = opcionPosicion


				modificador.rect.x = random.randrange((ANCHO/9), (ANCHO-120))
				# modificador.rect.y = - 10000

				# - agrego mi modificador a la lista de todos los elementos del juego
				todos.add(modificador)

				controlCantidadModificadores -= 1

		# ------------------------------------------------------------------
		# Control balas
		# ------------------------------------------------------------------

		for bala in balas:

			# ------------------------------------------------------------------
			# Colisión con los muros
			# ------------------------------------------------------------------

			chocarMuros = pygame.sprite.spritecollide(bala, muros, False)
			for muro in chocarMuros:
				balas.remove(bala)
				todos.remove(bala)

			# ------------------------------------------------------------------
			# Eliminar enemigos
			# ------------------------------------------------------------------

			eliminarElemento = pygame.sprite.spritecollide(bala, enemigos, False)
			for enemigo in eliminarElemento:
				enemigo.quitarVida(bala.damage)

				if enemigo.tipoEnemigo == 1:
					print "tengo, ", contador_chasqueador	
					if enemigo.vida <= 0:
						print "elimine un chasqueador"
						enemigos.remove(enemigo)
						todos.remove(enemigo)
						print "me quedan ", contador_chasqueador

				if enemigo.tipoEnemigo == 2:

					if enemigo.vida <= 0:
						print "elimine un bulimico"
						enemigos.remove(enemigo)
						todos.remove(enemigo)

				if enemigo.tipoEnemigo == 3:

					if enemigo.vida <= 0:
						print "elimine un murcielago"
						enemigos.remove(enemigo)
						todos.remove(enemigo)


				if enemigo.tipoEnemigo == 4:

					if enemigo.vida <= 0:
						print "elimine una calavera"
						enemigos.remove(enemigo)
						todos.remove(enemigo)

		# ------------------------------------------------------------------
		# muerte de juan perez
		# ------------------------------------------------------------------

		for enemigo in enemigos:

			eliminarJuanperez = pygame.sprite.spritecollide(enemigo, principal, False)
			for juanperez in eliminarJuanperez:
				juanperez.quitarVida(enemigo.damage)

				if juanperez.vida <= 0:
					principal.remove(juanperez)
					todos.remove(juanperez)

		# ------------------------------------------------------------------
		# Recolectar modificadores
		# ------------------------------------------------------------------
		
		for modificador in modificadores:

			recolectarModificadores = pygame.sprite.spritecollide(modificador, principal, False)
			for juanperez in recolectarModificadores:
				juanperez.aumentarVida(modificador.modificarPersonaje)
				modificadores.remove(modificador)
				todos.remove(modificador)

		# ------------------------------------------------------------------
		# GAME OVER
		# ------------------------------------------------------------------

		if juanperez.vida == 0:
			print "GAME OVER!!!!"
			fin = True
			

		# ------------------------------------------------------------------
		# Enfrentamiento con el jefe del nivel 1
		# ------------------------------------------------------------------

		if len(enemigos) == 0:
			print "la lista de enemigos está vacía"

		# if posicion_nivel_actual == 0:

			# ------------------------------------------------------------------
			# Control salida del jefe
			# ----------------------------------------------------------------

			while controlBossNivel1 > 0:

				drSalvador = Boss(1, 1000, 5)
				drSalvador.player = juanperez
				jefePrimerNivel.add(drSalvador)
				drSalvador.rect.x = random.randrange(850, 900)
				drSalvador.rect.y = ALTO - drSalvador.rect.height
				todos.add(drSalvador)

				controlBossNivel1 -= 1

			# ------------------------------------------------------------------
			# Muerte del jefe
			# ------------------------------------------------------------------

			for bala in balas:

				matarDrSalvador = pygame.sprite.spritecollide(bala, jefePrimerNivel, False)
				for drSalvador in matarDrSalvador:
					drSalvador.quitarVida(bala.damage)

					if drSalvador.vida <= 0:
						jefePrimerNivel.remove(drSalvador)
						todos.remove(drSalvador)
						posicion_nivel_actual = 1

			# ------------------------------------------------------------------
			# Muerte de juanperez
			# ------------------------------------------------------------------

			for jefe in jefePrimerNivel:

				eliminarJuanperez = pygame.sprite.spritecollide(jefe, principal, False)
				for juanperez in eliminarJuanperez:
					juanperez.quitarVida(jefe.damage)
					efectoMotocierra.play()

					if juanperez.vida <= 0:
						principal.remove(juanperez)
						todos.remove(juanperez)

		# ------------------------------------------------------------------
		# Cambio de nivel
		# ------------------------------------------------------------------

		if drSalvador.vida <= 0:
			posicion_nivel_actual = 1

		if posicion_nivel_actual == 0:
			nivel_actual = niveles[posicion_nivel_actual]

		if posicion_nivel_actual == 1:

			main2()

		fin = False
			# print "cambio al nivel 2"
			# nivel_actual = niveles[posicion_nivel_actual]


		# ------------------------------------------------------------------
		# Cambia la animación de los sprites de los personajes
		# ------------------------------------------------------------------

		#juanperez.image = Jugador[juanperez.direccion][0 + juanperez.contador]
		# chasqueador.image = zombieMordedor[0][0]

		# ------------------------------------------------------------------
		# Actualización de la pantalla
		# ------------------------------------------------------------------

		pantalla.blit(nivel_actual.ventana,(0,0))
		todos.update()
		todos.draw(pantalla)
		pygame.display.flip()
		reloj.tick(60)
