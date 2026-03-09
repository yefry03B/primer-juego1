

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