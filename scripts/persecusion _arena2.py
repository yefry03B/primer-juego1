import pygame
import sys

import math

import heapq
import random

import json
import os



# ==============================

# CONFIGURACIÓN

# ==============================


TAM_CELDA = 40

pygame.init()


pygame.mixer.init()

pygame.mixer.music.load("main.py/assets/music/musica.mp3")

pygame.mixer.music.play(-1)


pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Persecusion en la Arena")

reloj= pygame.time.Clock()

fuente = pygame.font.SysFont("Arial", 24)


pantalla_completa = False

volumen = 0.5

pygame.mixer.music.set_volume(volumen)


ANCHO, ALTO = 800, 600

FILAS = ALTO // TAM_CELDA

COLUMNAS = ANCHO // TAM_CELDA


ARCHIVO_GUARDADO = "progreso.json"


jugador = pygame.transform.scale(pygame.image.load("main.py/assets/imagen/jugador.png").convert_alpha(),(TAM_CELDA, TAM_CELDA))

enemigo = pygame.transform.scale(pygame.image.load("main.py/assets/imagen/enemigo.png").convert_alpha(),(TAM_CELDA, TAM_CELDA))

arenas = [
    pygame.transform.scale(pygame.image.load("main.py/assets/imagen/arena1.jpg").convert_alpha(),(800,600)),
    pygame.transform.scale(pygame.image.load("main.py/assets/imagen/arena2.jpg").convert_alpha(),(800,600)),
    pygame.transform.scale(pygame.image.load("main.py/assets/imagen/arena3.jpg").convert_alpha(),(800,600)),
    pygame.transform.scale(pygame.image.load("main.py/assets/imagen/arena4.jpg").convert_alpha(),(800,600))
]

muro = pygame.transform.scale(pygame.image.load("main.py/assets/imagen/muro.png").convert_alpha(),(TAM_CELDA, TAM_CELDA))

puerta_img = pygame.transform.scale( pygame.image.load("main.py/assets/imagen/puerta.png").convert_alpha(),(TAM_CELDA, TAM_CELDA))

fragmento = pygame.transform.scale(pygame.image.load("main.py/assets/imagen/fragmento.png").convert_alpha(),(TAM_CELDA, TAM_CELDA))

sonido_fragmento = pygame.mixer.Sound("main.py/assets/sounds/fragmento.wav")


# ==============================

# COLORES

# ==============================


BLANCO = (255,255,255)

NEGRO = (0,0,0)

AZUL = (50,100,255)

ROJO = (200,50,50)

GRIS = (120,120,120)

VERDE = (50,200,100)

AMARILLO = (255,215,0)

MORADO = (150,0,200)


# ==============================

# PANTALLA COMPLETA

# ==============================


def alternar_pantalla():

    global pantalla, pantalla_completa, ANCHO, ALTO, FILAS, COLUMNAS

    if pantalla_completa:

        pantalla = pygame.display.set_mode((800, 600))

        ANCHO, ALTO = 800, 600

        pantalla_completa = False

    else:

        info = pygame.display.Info()

        ANCHO, ALTO = info.current_w, info.current_h

        pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)

        pantalla_completa = True


    FILAS = ALTO // TAM_CELDA

    COLUMNAS = ANCHO // TAM_CELDA


# ==============================

# GUARDADO

# ==============================


def guardar_progreso(nivel):

    with open(ARCHIVO_GUARDADO, "w") as f:

        json.dump({"nivel": nivel}, f)


def cargar_progreso():

    if os.path.exists(ARCHIVO_GUARDADO):

        with open(ARCHIVO_GUARDADO, "r") as f:

            return json.load(f).get("nivel",1)

    return 1


# ==============================

# MENÚ VOLUMEN

# ==============================


def menu_volumen():

    global volumen

    while True:

        pantalla.fill(NEGRO)

        texto = fuente.render(f"VOLUMEN: {int(volumen*100)}%", True, BLANCO)


        subir_rect = pygame.Rect(300,250,200,50)

        bajar_rect = pygame.Rect(300,320,200,50)

        volver_rect = pygame.Rect(300,390,200,50)


        pygame.draw.rect(pantalla, VERDE, subir_rect)

        pygame.draw.rect(pantalla, ROJO, bajar_rect)

        pygame.draw.rect(pantalla, AZUL, volver_rect)


        pantalla.blit(texto,(300,180))

        pantalla.blit(fuente.render("SUBIR",True,NEGRO), subir_rect.move(60,10))

        pantalla.blit(fuente.render("BAJAR",True,NEGRO), bajar_rect.move(60,10))

        pantalla.blit(fuente.render("VOLVER",True,NEGRO), volver_rect.move(50,10))


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if subir_rect.collidepoint(evento.pos):

                    volumen = min(1.0, volumen+0.1)

                if bajar_rect.collidepoint(evento.pos):

                    volumen = max(0.0, volumen-0.1)

                if volver_rect.collidepoint(evento.pos):
                    return

                pygame.mixer.music.set_volume(volumen)

        pygame.display.flip()

        reloj.tick(60)


# ==============================

# MENÚ PRINCIPAL

# ==============================


def menu():

    while True:

        pantalla.fill(NEGRO)

        titulo = fuente.render("PERSECUSION EN LA ARENA", True, BLANCO)


        iniciar_rect = pygame.Rect(280,230,240,50)

        volumen_rect = pygame.Rect(280,300,240,50)

        salir_rect = pygame.Rect(280,370,240,50)


        pygame.draw.rect(pantalla, VERDE, iniciar_rect)

        pygame.draw.rect(pantalla, AZUL, volumen_rect)

        pygame.draw.rect(pantalla, ROJO, salir_rect)


        pantalla.blit(titulo,(280,150))

        pantalla.blit(fuente.render("INICIAR JUEGO",True,NEGRO), iniciar_rect.move(30,10))

        pantalla.blit(fuente.render("CONFIGURACIÓN",True,NEGRO), volumen_rect.move(35,10))

        pantalla.blit(fuente.render("SALIR",True,NEGRO), salir_rect.move(70,10))


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if iniciar_rect.collidepoint(evento.pos):
                    return

                if volumen_rect.collidepoint(evento.pos):

                    menu_volumen()

                if salir_rect.collidepoint(evento.pos):

                    pygame.quit(); sys.exit()

        pygame.display.flip()

        reloj.tick(60)


# ==============================

# MAPA

# ==============================


def crear_mapa(nivel):

    mapa = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

    num_obstaculos = 5 + nivel*2

    for _ in range(num_obstaculos):

        alto_obs = random.randint(1,3)

        ancho_obs = random.randint(3,8)

        x = random.randint(1, FILAS-alto_obs-1)

        y = random.randint(1, COLUMNAS-ancho_obs-1)

        for i in range(alto_obs):

            for j in range(ancho_obs):

                mapa[x+i][y+j] = 1
    return mapa


# ==============================

# A*

# ==============================


def heuristica(a,b):

    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def vecinos(nodo,mapa):

    movimientos = [(1,0),(-1,0),(0,1),(0,-1)]

    lista=[]

    for m in movimientos:

        nx = nodo[0] + m[0]

        ny = nodo[1] + m[1]

        if 0<=nx<FILAS and 0<=ny<COLUMNAS:

            if mapa[nx][ny]==0:

                lista.append((nx,ny))
    return lista


def a_estrella(inicio,fin,mapa):

    abiertos=[]

    heapq.heappush(abiertos,(0,inicio))

    vino_de={}

    costo={inicio:0}

    while abiertos:

        actual = heapq.heappop(abiertos)[1]

        if actual == fin:

            camino=[]

            while actual in vino_de:

                camino.append(actual)

                actual = vino_de[actual]

            camino.reverse()

            return camino

        for v in vecinos(actual,mapa):

            nuevo = costo[actual]+1

            if v not in costo or nuevo<costo[v]:

                costo[v] = nuevo

                prioridad = nuevo + heuristica(v,fin)

                heapq.heappush(abiertos,(prioridad,v))

                vino_de[v]=actual

    return []


# ==============================

# CLASES

# ==============================


class Jugador:

    def __init__(self):

        self.x=1

        self.y=1

        self.vida=100
        self.fragmentos=0

    def mover(self,dx,dy,mapa):

        nx=self.x+dx

        ny=self.y+dy

        if 0<=nx<FILAS and 0<=ny<COLUMNAS and mapa[nx][ny]==0:

            self.x=nx
            self.y=ny

    def dibujar(self): 

        offset = math.sin(pygame.time.get_ticks()/200)*2

        pantalla.blit(jugador,(self.y*TAM_CELDA,self.x*TAM_CELDA+offset))


class Enemigo:

    def __init__(self,nivel,mapa):

        while True:

            x=random.randint(FILAS//2,FILAS-2)

            y=random.randint(COLUMNAS//2,COLUMNAS-2)

            if mapa[x][y]==0:
                self.x=x
                self.y=y
                break

        self.daño=5+nivel

    def actualizar(self,jugador,mapa):

        dist=abs(self.x-jugador.x)+abs(self.y-jugador.y)

        if dist<=1:

            jugador.vida-=self.daño

        else:

            camino=a_estrella((self.x,self.y),(jugador.x,jugador.y),mapa)

            if camino:

                self.x,self.y=camino[0]

    def dibujar(self):

        pantalla.blit(enemigo,(self.y*TAM_CELDA,self.x*TAM_CELDA))


def dibujar_barra_vida(jugador):

    vida=max(0,min(jugador.vida,100))

    pygame.draw.rect(pantalla,ROJO,(10,40,200,20))

    pygame.draw.rect(pantalla,VERDE,(10,40,vida*2,20))


# ==============================

# GAME OVER

# ==============================


def game_over():

    while True:

        pantalla.fill(NEGRO)

        pantalla.blit(fuente.render("GAME OVER",True,ROJO),(350,250))

        pantalla.blit(fuente.render("CLICK PARA VOLVER",True,BLANCO),(250,300))

        for evento in pygame.event.get():

            if evento.type==pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type==pygame.MOUSEBUTTONDOWN:

                guardar_progreso(1)
                return
        pygame.display.flip()

        reloj.tick(60)


# ==============================

# YOU WIN

# ==============================


def you_win():

    while True:

        pantalla.fill(NEGRO)

        pantalla.blit(fuente.render("¡¡YOU WIN!!", True, VERDE), (330, 250))

        pantalla.blit(fuente.render("CLICK PARA VOLVER AL MENU", True, BLANCO), (220, 300))


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                pygame.quit(); sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:

                guardar_progreso(1)
                return

        pygame.display.flip()

        reloj.tick(60)


# ==============================

# JUEGO

# ==============================


def juego():

    nivel = cargar_progreso()

    while True:

        mapa = crear_mapa(nivel)

        jugador = Jugador()

        enemigos = [Enemigo(nivel,mapa) for _ in range(1+nivel)]

        puerta = (FILAS-1, COLUMNAS-1)


        fragmentos=[]

        while len(fragmentos)<4:

            f_x=random.randint(1,FILAS-3)

            f_y=random.randint(1,COLUMNAS-4)

            if mapa[f_x][f_y]==0:

                fragmentos.append((f_x,f_y))


        while True:

            reloj.tick(5+nivel)

            for evento in pygame.event.get():

                if evento.type == pygame.QUIT:

                    pygame.quit(); sys.exit()

                if evento.type == pygame.KEYDOWN:

                    if evento.key==pygame.K_ESCAPE:
                        return

                    if evento.key==pygame.K_F11:
                        alternar_pantalla()


            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_w]: jugador.mover(-1,0,mapa)

            if teclas[pygame.K_s]: jugador.mover(1,0,mapa)

            if teclas[pygame.K_a]: jugador.mover(0,-1,mapa)

            if teclas[pygame.K_d]: jugador.mover(0,1,mapa)


            for enemigo in enemigos:

                enemigo.actualizar(jugador,mapa)


            if jugador.vida<=0:

                game_over()
                return


            if (jugador.x,jugador.y) in fragmentos:

                fragmentos.remove((jugador.x,jugador.y))

                jugador.fragmentos+=1

                sonido_fragmento.play()


            if jugador.fragmentos>=3 and (jugador.x,jugador.y)==puerta:

                nivel += 1

                if nivel > 4:

                    you_win()
                    return

                guardar_progreso(nivel)

                break


            pantalla.fill(NEGRO)

            pantalla.blit(arenas[(nivel-1)%len(arenas)],(0,0))


            for i in range(FILAS):

                for j in range(COLUMNAS):

                    if mapa[i][j]==1:

                        pantalla.blit(muro,(j*TAM_CELDA,i*TAM_CELDA,TAM_CELDA,TAM_CELDA))


            for f in fragmentos:

                pantalla.blit(fragmento,(f[1]*TAM_CELDA,f[0]*TAM_CELDA))

          
            pantalla.blit(puerta_img,(puerta[1]*TAM_CELDA, puerta[0]*TAM_CELDA))


            jugador.dibujar()

            for enemigo in enemigos:

                enemigo.dibujar()


            dibujar_barra_vida(jugador)


            pantalla.blit(fuente.render(f"Fragmentos: {jugador.fragmentos}/3  Nivel: {nivel}",True,BLANCO),(10,10))

            pygame.display.flip()


# ==============================

# EJECUCIÓN

# ==============================


if __name__ == "__main__":

    while True:
        menu()

        juego()
        