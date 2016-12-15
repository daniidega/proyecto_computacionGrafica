import pygame
import random


ANCHO=800
ALTO=500

BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
MARRON=(153,76,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, imagen_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen_sprite
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        self.var_x=5
        self.var_y=0
        self.con=0
        self.direccion=2

    def gravedad(self):
        if self.var_y ==0:
            self.var_y =1
        else:
            self.var_y+=0.35

        if self.rect.y >= ALTO-50-self.rect.height: #se detiene el objeto en la parte de abajo
            self.rect.bottom = ALTO #bottom la parte de abajo del objeto, top la parte de arriba
            self.var_y=0    

    def update(self):
        self.gravedad()
        self.rect.x+=self.var_x
        l_col=pygame.sprite.spritecollide(self,self.lp,False)
        for pl in l_col:
            if self.var_x>0:
                self.rect.right=pl.rect.left
            else:
                self.rect.left=pl.rect.right
        if self.rect.right > ANCHO-10:
            self.rect.right=ANCHO-10
            self.var_x=0
        if self.rect.left < 0+10:
            self.rect.left=0+10
            self.var_x=0        

        self.rect.y+=self.var_y
        l_col=pygame.sprite.spritecollide(self,self.lp,False) #lista de colisiones
        for pl in l_col:
            if self.var_y>0:
                self.rect.bottom=pl.rect.top
                if pl.var_y!=0:
                    self.rect.y+=pl.var_y
            else:
                self.rect.top=pl.rect.bottom
            self.var_y=0

class Enemigo(pygame.sprite.Sprite): #Clase, Sprite=Superclase
    def __init__(self,archivo): #Costructor
        pygame.sprite.Sprite.__init__(self) # inicializo mi Super Clase
        self.image=pygame.image.load(archivo).convert_alpha() #atributos de la clase comienzan con self
         #el atributo image es heredado
        self.rect=self.image.get_rect() #rect variable tambien es heredada de la super clase Sprite
        self.rect.x=0
        self.rect.y=0
        self.var_x=-5  #variacion en x
        self.var_y=3
        self.disparar=False  #como hacer para que el enemigo dispare
        self.vida=3
        self.tiempo=random.randrange(100) #dispara rapido o lento


    def update(self):       #metodo actualizar heredado de Sprite
        self.rect.y+=self.var_y  # se mueve en la pantalla de a 5 posiciones
        self.tiempo-=1
        if self.tiempo==0:
            self.disparar=True
            self.tiempo=random.randrange(20)

class Bloque(pygame.sprite.Sprite):
    def __init__(self,an,al,px,py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([60,30])
        self.image.fill(MARRON)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
        self.rect.x=px
        self.rect.y=py
        self.var_y=0
        self.limitesuperior=50
        self.limiteinferior=400
        self.limiteder=600
        self.limiteizq=250

    def update(self):
        self.rect.x+=self.var_x  
        if self.rect.x>self.limiteinferior:
            self.var_x=self.var_x*(-1)
        if self.rect.x<self.limitesuperior:
            self.var_x=self.var_x*(-1)

        self.rect.y+=self.var_y
        if self.rect.y>self.limiteinferior:
            self.var_y=self.var_y*(-1)
        if self.rect.y<self.limitesuperior:
            self.var_y=self.var_y*(-1)

class Bala(pygame.sprite.Sprite): #Clase, Sprite=Superclase
    def __init__(self,archivo): #Costructor
        pygame.sprite.Sprite.__init__(self) # inicializo mi Super Clase
        self.image=pygame.image.load(archivo).convert_alpha() #atributos de la clase comienzan con self
         #el atributo image es heredado
        self.rect=self.image.get_rect() #rect variable tambien es heredada de la super clase Sprite
        self.rect.x=0
        self.rect.y=0
        self.var_x=10  #variacion en x
        self.direccion=0 #direccion de la bala del enemigo

    def update(self):       #metodo actualizar heredado de Sprite
        if self.direccion==1:
            self.var_x=-10
        self.rect.x+=self.var_x            

def Recortar(archivo, anc, alc):
    matriz=[] #varfiable para guardar los recortes (cuadritos)
    imagen=pygame.image.load(archivo).convert_alpha()
    i_ancho, i_alto=imagen.get_size() #muestra el tamano del fondo que cargamos
    print i_ancho,' ',i_alto
    for x in range(0, i_ancho/anc): #anc:ancho de corte, alc:alto de corte
        linea=[]
        for y in range(0,i_alto/alc):
            cuadro=(x*anc, y*alc, anc, alc)
            linea.append(imagen.subsurface(cuadro)) #mapa de lo que tiene que Recortar
        matriz.append(linea)
    return matriz        


def main2():
    pygame.init()                                       #inicializacion del juego
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    fondo=pygame.image.load('fondo2.jpg') #carga la imagen guardada
    dimensiones_fondo=fondo.get_rect()
    ventana=fondo.subsurface(0,300,ANCHO, ALTO) #recortar pedazos (pos_x,200)

    todos=pygame.sprite.Group()
    plataformas=pygame.sprite.Group()

    todos=pygame.sprite.Group()
    personaje=Recortar('juanperez.png',48,48)
    jp=Jugador(personaje[0][0])
    todos.add(jp)

    b=Bloque(100,30,200,400)
    plataformas.add(b)
    todos.add(b)

    b=Bloque(100,30,670,100)
    plataformas.add(b)
    todos.add(b)

    b=Bloque(100,30,400,250)
    plataformas.add(b)
    todos.add(b)

    b=Bloque(100,30,700,420)
    plataformas.add(b)
    todos.add(b)

    as1=Bloque(100,30,50,150) #ascensor
    as1.image.fill(MARRON)
    as1.var_y=2
    plataformas.add(as1)
    todos.add(as1)

    as1=Bloque(100,30,600,200) #ascensor
    as1.image.fill(MARRON)
    as1.var_y=2
    plataformas.add(as1)
    todos.add(as1)

    as1=Bloque(100,30,400,100) #ascensor derecha-izquierda
    as1.image.fill(MARRON)
    as1.var_x=2
    plataformas.add(as1)
    todos.add(as1)

    as1=Bloque(100,30,400,350) #ascensor derecha-izquierda
    as1.image.fill(MARRON)
    as1.var_x=2
    plataformas.add(as1)
    todos.add(as1)

    jp.lp=plataformas
    reloj=pygame.time.Clock()

    enemigos=pygame.sprite.Group()
    for i in range(10):
        en=Enemigo('nave3.png')
        en.rect.x=random.randrange(100,ANCHO)
        en.rect.y=random.randrange(ALTO-50)
        en.var_x=(-1)*random.randrange(3,10)
        enemigos.add(en) #lista de enemigos
        todos.add(en)
    balas=pygame.sprite.Group()
    ebalas=pygame.sprite.Group()

    var_y=-50 #var_y=-2
    pos_y=4110 #pos_y=500

    reloj=pygame.time.Clock()
    fin=False
    contenemigos=50
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    jp.var_x=-10
                    jp.var_y=0
                    jp.direccion=1
                if event.key == pygame.K_RIGHT:
                    jp.var_x=10
                    jp.var_y=0
                    jp.direccion=2
                if event.key == pygame.K_UP:
                    jp.var_y=-10
                    jp.var_x=0
                    jp.direccion=3
                if event.key == pygame.K_DOWN:
                    jp.var_y=10
                    jp.var_x=0
                    jp.direccion=0
                if event.key == pygame.K_SPACE:
                    b=Bala('Bala.png')
                    b.rect.x=jp.rect.x   #la bala sale aproximadamente donde esta el jugador
                    b.rect.y=jp.rect.y
                    balas.add(b)
                    todos.add(b)

                if event.key == pygame.K_0:
                    fin = False

        jp.image=personaje[0][0] #imagen que quiere recortar            

        #if jp.rect.right >= ANCHO-10:
         #   pos_x+=5 #pos_x+=pos_x
        #if jp.rect.left <= 10:
         #   pos_x-=5
        #if pos_x>=0 and pos_x < (dimensiones_fondo.width - ANCHO):
         #   ventana=fondo.subsurface(pos_x,300,ANCHO, ALTO) #recortar pedazos (pos_x,200)
        ls_choque=pygame.sprite.spritecollide(jp, enemigos,True)
        for elemento in ls_choque:
            print 'golpe'

        for en in enemigos:
            if en.rect.x < -100:
                enemigos.remove(en)

        if contenemigos == 0:
            en=Enemigo('nave3.png')
            en.rect.x=ANCHO
            en.rect.y=random.randrange(ALTO-50)
            en.var_x=(-1)*random.randrange(3,10)
            enemigos.add(en) #lista de enemigos
            todos.add(en)
            contenemigos=50
        else:
            contenemigos-=1

        for bl in balas:
            ls_impacto=pygame.sprite.spritecollide(bl,enemigos,True)
            for im in ls_impacto:
                balas.remove(bl) #quita las balas
                todos.remove(bl)
                im.vida-=1
                if im.vida==0:
                    enemigos.remove(im)
                    todos.remove(im)

        for en in enemigos:
            if en.disparar:
                print 'dips'
                be=Bala('Bala.png')
                be.direccion=1
                be.rect.x=en.rect.x
                be.rect.y=en.rect.y
                ebalas.add(be)
                todos.add(be)
                en.disparar=False
                     
        if jp.rect.top >= ALTO -4100:
            pos_y-=5 #pos_x+=pos_x
        if jp.rect.bottom <= ALTO-110:
            pos_y-=5
        if pos_y>=0 and pos_y < (dimensiones_fondo.height - ALTO):
            ventana=fondo.subsurface(5,pos_y,ANCHO, ALTO) #recortar pedazos (pos_x,200)
            #print pos_x
        pantalla.blit(ventana, (0,0))
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(20)
