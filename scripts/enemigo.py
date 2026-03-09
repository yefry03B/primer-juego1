
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
