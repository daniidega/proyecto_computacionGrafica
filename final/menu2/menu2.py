import pygame 
from pygame.locals import *
import random

ANCHO = 800
ALTO = 500

BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

def principal_menu():
        fondo=pygame.image.load("menu2/menuz.jpg")
        pantalla.fill(NEGRO)
        fuente3=pygame.font.SysFont('monospace',30) 
        fuente=pygame.font.Font('DEMON SKER.ttf', 90)
        valor=0
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
                                if (tecla[K_1]):
                                        valor=1
                                        fin=True
                                if (tecla[K_2]):
                                        valor=2
                                        fin=True
                                if (tecla[K_3]):
                                        valor=3
                                        fin=True
                                if (tecla[K_0]):
                                        valor=0
                                        fin=True
                pantalla.blit(fondo, (0,0))
                pantalla.blit(txt_menu, [50, 150])
                pantalla.blit(txt_menu1, [50, 320])
                pantalla.blit(txt_menu2, [50, 350])
                pantalla.blit(txt_menu4, [50, 380])
                pygame.display.flip()
        return valor

def Instrucciones():
        fondo=pygame.image.load("menu2/instrucciones.jpg")
        pantalla.fill(NEGRO)
        
        valor=0
        fin=False
        while not fin:
                tecla=pygame.key.get_pressed()
                for event in pygame.event.get():
                                if (tecla[K_x]):
                                        fin=True
  
                pantalla.blit(fondo, (0,0))
                pygame.display.flip()
                
if __name__ == '__main__':
        pygame.init()

        #Set the height and width of the screen
        tam = [ANCHO, ALTO]
        pantalla = pygame.display.set_mode(tam)
        pygame.display.set_caption("Espartan Perdido")
       # from Libreria import *
        Salida=False
        while (not Salida):
                accion=principal_menu()
                if(accion==1):
                        pygame.mixer.music.stop()
                        main()
                if(accion==2):
                        Instrucciones()
                if(accion==0):
                        Salida=True




