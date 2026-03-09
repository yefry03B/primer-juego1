
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