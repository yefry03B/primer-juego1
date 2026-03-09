#---------------
# JUGADOR
#---------------

# YEFRY BERAS = 22-MISN-2-040

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