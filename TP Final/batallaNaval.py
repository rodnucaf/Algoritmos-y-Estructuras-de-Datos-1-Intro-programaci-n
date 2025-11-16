from typing import Any
from biblioteca import *


## Ejercicio 1
def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    
    """ 
    Indica la cantidad de barcos de tamaño "tamaño"
    PRE: los barcos son válidos (osea que solo se encuentren de forma vertical 
        u horizontal (no en diagonal), su tamaño sea de 2 a 5 posiciones, 
        y que no se pisen las posiciones entre un barco y otro)  
    Args:
        barco(list[BarcoEnGrilla]) : Una lista con los barcos (sus posiciones en la grilla)    
    Returns:
        la cantidad (int) de barcos del tamaño pedido  
    
    """
    cantidad: int = 0
    for barco in barcos:
        if len(barco) == tamaño:
            cantidad += 1
    return cantidad

#ejercicio 2 


def nuevoJuego(cantidadDeFilas: int, cantidadDeColumnas: int, barcosDisponibles: list[Barco]) -> EstadoJuego:
    """
    Inicializa un nuevo juego de Batalla Naval con todas las estructuras necesarias.

    Esta función crea un estado de juego completo, incluyendo:
    - Las dimensiones del tablero.
    - La lista de barcos disponibles para los jugadores.
    - El turno inicial del jugador UNO.
    - Los tableros de ambos jugadores con todas las celdas vacías.

    Funciones internas:

    Args:
    
    cantidadDeFilas : int
        Número de filas de cada tablero.
    cantidadDeColumnas : int
        Número de columnas de cada tablero.
    barcosDisponibles : list[Barco]
        Lista con las longitudes de los barcos que estarán disponibles en la partida.

    Retorna:
    --------
    EstadoJuego
        Tupla que representa el estado completo del juego:
        (dimensiones: tuple[int, int],
         barcosDisponibles: list[Barco],
         turno: list[Jugador],
         tableroJugador1: Tablero,
         tableroJugador2: Tablero)
         
        Cada Tablero es una tupla (grilla_local, grilla_oponente),
        y cada Grilla es una lista de listas con todas las celdas inicializadas con VACÍO.
    """
 

    
    turno: list[Jugador] = [UNO]
    dimensionesNuevoJuego : Dimensiones= (cantidadDeFilas,cantidadDeColumnas)
    tableroUNO:Tablero= nuevoTablero(cantidadDeFilas,cantidadDeColumnas)
    tableroDOS:Tablero= nuevoTablero(cantidadDeFilas,cantidadDeColumnas)
    estadoJuegoNuevo: EstadoJuego = (dimensionesNuevoJuego, barcosDisponibles, turno, tableroUNO, tableroDOS)
 
    return estadoJuegoNuevo

def grillaVacía(cantidadDeFilas:int, cantidadDeColumnas:int)-> Grilla:
        
        grilla:Grilla=[]
        for _ in range (cantidadDeFilas):
            fila:list[Celda]=[]
            for _ in range(cantidadDeColumnas):
                fila.append(VACÍO)
            grilla.append(fila)
        return grilla
    
        
def nuevoTablero(cantidadDeFilas:int, cantidadDeColumnas:int)->Tablero:
        
        grilla_local:Grilla    = grillaVacía(cantidadDeFilas, cantidadDeColumnas)
        grilla_oponente:Grilla = grillaVacía(cantidadDeFilas, cantidadDeColumnas)

        tablero: Tablero = (grilla_local, grilla_oponente)
        
        return tablero

## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Verifica que el estado del juego *estadoDeJuego* sea válido. Devuelve True si:
        -La cantidad de filas en *estadoDeJuego* es mayor o igual a 1 y menor o igual a 26.
        -La cantidad de columnas en *estadoDeJuego* es mayor estricto que 0.
        -La longitud de *estadoDeJuego[2]* es igual a 1, es decir, hay sólo un turno activo.
        -la lista de barcos disponibls es mayor a cero.
        -son válidos los tableros de los jugadores: son válidas las grillas, coinciden con las dimensiones y
        los barcos de la grilla local son iguales en tamaño y cantidad con los de *estadoDeJuego*
        -Coinciden las posiciones atacadas en ambos tableros y la diferencia de celdas atacadas entre ambos es
        mayor o igual que 0 y menor o igual que 1.

        PRE: True

        Args:
            estadoDeJuego (EstadoJuego): El estado actual de la partida

        Returns
            True si el estado es válido, False si no.
    """
    res:list[bool] = []
    res.append(esEstadoValidoFilas(estadoDeJuego))
    
    res.append(esEstadoValidoTurno(estadoDeJuego))
    
    res.append(esEstadoValidoColumnas(estadoDeJuego))
    
    res.append(esEstadoValidoBarcos(estadoDeJuego))
    
    res.append(tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego))
    
    res.append(tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego))
    
    res.append(coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO),tableroDeJugador(estadoDeJuego, DOS)))
    
    for i in range (0, len(res), 1):
        if res[i] == False:
            return False
        
    return True

def esEstadoValidoFilas(estadoDeJuego:EstadoJuego)->bool:

    return cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1 and cantidadDeFilasEstadoJuego(estadoDeJuego) <=26

def esEstadoValidoTurno(estadoDeJuego:EstadoJuego) -> bool:
    return len(estadoDeJuego[2]) == 1

def esEstadoValidoColumnas(estadoDeJuego:EstadoJuego)->bool:
    return cantidadDeColumnasEstadoJuego(estadoDeJuego) >0

def esEstadoValidoBarcos(estadoDeJuego:EstadoJuego)->bool:
    return len(barcosDisponibles(estadoDeJuego)) > 0

def tamaños(barcos:list[BarcoEnGrilla])->list[int]:
    res:list[int] = []
    
    for i in range(0,len(barcos),1):
        res.append(tamañoBarco(barcos[i]))

    return res

def mismosElementos(listaUno:list, listaDos:list)->bool:

    return coincidenTamañosDeListas(listaUno, listaDos) and mismosElementosAux(listaDos, listaUno) and mismosElementosAux(listaUno, listaDos)
 

def mismosElementosAux(listaUno:list, listaDos:list)->bool:

    for elemento in listaUno:

        if cantidadDeApariciones(elemento, listaUno) != cantidadDeApariciones(elemento, listaDos):
            return False
    
    return True  

def coincidenTamañosDeListas(listaUno:list, listaDos:list)->bool:
    tamañoListaUno:int = len(listaUno)
    tamañoListaDos:int = len(listaDos)

    return tamañoListaUno == tamañoListaDos

def coincidenBarcosEnGrilla(barcos:list[Barco], grilla:Grilla)->bool:
    barcosEnLaGrilla:list[int] = tamaños(barcosEnGrilla(grilla))

    return mismosElementos(barcos, barcosEnLaGrilla)

def compararPosicionDeTablero(tablero:Tablero, tableroOponente:Tablero)->bool:
    cantFilas:int = len(tablero[0])
    cantColumnas:int = len(tablero[0][0])
    

    for i in range (0,cantFilas,1):
        for j in range (0,cantColumnas,1):
            if not celdaEsVacío(tablero[1][i][j]):
                if not celdasTienenMismoContenido(tablero[1][i][j], tablero[0][i][j]):
                    return False
    
    return True

def celdasTienenMismoContenido(celda:Celda, celdaDos:Celda)->bool:
    return celda == celdaDos

def celdaEsVacío(celda:Celda)->bool:
    return celda == VACÍO

def cantPosicionesNoVacias(grilla:Grilla)->int:
    
    res:int = 0

    for i in range(0,len(grilla),1):

        for j in range (0,len(grilla[0]),1):

            celdaAEvaluar:Celda = grilla[i][j]

            if not celdaEsVacío(celdaAEvaluar):
                res = res +1

    return res

def coincidenPosicionesAtacadas(tablero:Tablero, tableroOponente:Tablero)->bool:
    res:bool

    if not (compararPosicionDeTablero(tablero, tableroOponente) and compararPosicionDeTablero(tableroOponente, tablero)):
        res = False
    else:
        nUno:int = cantPosicionesNoVacias(grillaOponente(tablero))
        nDos:int = cantPosicionesNoVacias(grillaOponente(tableroOponente))

        res = nUno-nDos >= 0 and nUno-nDos <=1 
    
    return res
    

def tableroValidoEnJuego (tablero:Tablero, estadoDeJuego:EstadoJuego)->bool:
    return grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))


## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ 
    Se hace un disparo del jugador que tiene el turno actual en la posición *posición* elegida hacia
    la grilla del oponente. Actualiza las celdas en las grillas correspondientes y cambia el turno.
    Modifica *estado_juego*. Devuelve el resultado del disparo.

    PRE: esEstadoDeJuegoVálido(estado_juego)
    PRE:  esPosiciónVálidaEnGrilla(posición, grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))))

    Args:
        estado_juego: (estadoJuego): Estado actual de la partida.
        posición (Posición): La posición en la que se desea disparar.

    Returns:
        Devuelve NADA si no se impactó un barco. TOCADO si sí.     
    """
    jugadorActual:Jugador = turno(estado_juego)
    jugadorOponente:Jugador = obtenerJugadorOponente(estado_juego)

    tableroActual:Tablero = tableroDeJugador(estado_juego, jugadorActual)
    tableroOponente:Tablero = tableroDeJugador(estado_juego, jugadorOponente)

    grillaOponenteLocal = grillaLocal(tableroOponente)
    grillaOponenteVisible = grillaOponente(tableroActual)

    res:ResultadoDisparo

    if disparoHaceAgua(estado_juego, posición):
        res = NADA
        cambiarCeldaGrilla(grillaOponenteLocal, posición, AGUA)
        cambiarCeldaGrilla(grillaOponenteVisible, posición, AGUA)
    else:
        cambiarCeldaGrilla(grillaOponenteVisible, posición, BARCO)
        res = TOCADO

    cambiarTurno(estado_juego)
    return res

def obtenerJugadorOponente(estadoDeJuego:EstadoJuego)->Jugador:

    jugadorActual:Jugador = turno(estadoDeJuego)

    if jugadorActual == UNO:
        return DOS
    
    return UNO

def disparoHaceAgua(estadoDeJuego:EstadoJuego, posicion: Posición)->bool:

    jugador_oponente = obtenerJugadorOponente(estadoDeJuego)

    return celdaEsVacío(celdaEnPosición(grillaLocal(tableroDeJugador(estadoDeJuego, jugador_oponente)),posicion)) #== VACÍO

## Ejercicio 5


def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ dada una Grilla te da las posicion de los barcos en la grilla
    PRE: la grilla es válida (es una matriz cuadrada y menor a 26(letras del abecedario))
        hay una única forma de contruir barcos, osea que dada un a posicion, solo puedo encontrar
        otro barco hacia la derecha/izquierda o arriba/abajo (no se permiten barcos adyacentes)
    Args:
        grilla (Grilla): Una grilla de la que obtener barcos.
    Returns: 
        una lista de las posiciones de los barcos en la grilla
    """
    barquitos: list[BarcoEnGrilla] = []
    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    visitadas: list[list[bool]] = crearGrillaDePosicionesNoVisitadas(grilla)

    for i in range(filas):
        for j in range(columnas):
            celdaActual: bool = celdaEsBarco(grilla[i][j])
            visitada: bool = visitadas[i][j]

            if celdaActual and not visitada:
                indice: tuple[int, int] = (i, j)
                barco: BarcoEnGrilla = construirBarcoDesde(grilla, visitadas, indice)
                barquitos.append(barco)
    return barquitos

def construirBarcoDesde(grilla: Grilla, visitadas: list[list[bool]], indice: tuple[int,int]) -> BarcoEnGrilla:
    barco: BarcoEnGrilla = []

    fila: int = indice[0]
    col: int = indice[1]
    posicionActual: Posición = obtenerPosiciónDesdeIndiceDeGrilla(fila, col)
    
    barco.append(posicionActual)
    visitadas[fila][col] = True

    direcciones: list[Dirección] = direccionesOrtogonales()

    for direccion in direcciones:
        filaDir: int = fila
        colDir: int = col
        posicionDir: Posición = posicionActual

        hayBarco: bool = celdaEsBarco(grilla[fila][col])
        while hayBarco:
            if hayPosiciónAdyacenteAl(grilla, posicionDir, direccion):
                siguiente: Posición = posiciónAdyacenteAl(grilla, posicionDir, direccion)
                filaSig: int = obtenerIndiceDesdePosicion(siguiente)[0]
                colSig: int = obtenerIndiceDesdePosicion(siguiente)[1]

                esBarco: bool = celdaEsBarco(grilla[filaSig][colSig])
                noVisitada: bool = not visitadas[filaSig][colSig]

                if esBarco and noVisitada:
                    barco.append(siguiente)
                    visitadas[filaSig][colSig] = True
                    filaDir = filaSig
                    colDir = colSig
                    posicionDir = siguiente
                else:
                    hayBarco = False
            else:
                hayBarco = False

    return barco

def celdaEsBarco(celda:Celda)->bool:

    return celda == BARCO

def crearGrillaDePosicionesNoVisitadas(grilla:Grilla)->list[list[bool]]:

    filas:int = len(grilla)
    columans:int = len(grilla[0])

    res:list[list[bool]] = []

    for i in range (0, filas, 1):

        res.append([])

        for j in range (0, columans, 1):

            res[i].append(False)

    return res

def obtenerPosiciónDesdeIndiceDeGrilla(fila:int, columna:int)->Posición:

    listaLetras:list[str] = letras()

    posición:Posición = (listaLetras[fila], columna + 1)

    return posición

def obtenerIndiceDesdePosicion(posicion:Posición)->tuple[int,int]:

    fila:int
    listaLetras:list[str] = letras()

    for i in range (0, len(listaLetras),1):
        if posicion[0] == listaLetras[i]:
            fila = i

    
    indice:tuple[int,int] = (fila, posicion[1]-1)
    return indice

def letras()->list[str]:
    letras:list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","Ñ", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y","Z"]
    return letras

#EJERCICIO 6

def elJugadorConMejorPuntería(estadoDeJuego:EstadoJuego)->Jugador:
    """ Dado un EstadoJuego devuelve el jugador con mejor puntería. Es decir, el jugador que haya descubierto
    más barcos (sin importar si descubrió todas sus posiciones) en relación a las celdas descubiertas con AGUA
    PRE:
        -El estado de juego es un EstadoJuego válido.
        -Los jugadores no tienen la misma puntería.

    Args: estadoDeJuego (EstadoJuego): El estado actual de la partida.

    Returns: 
        Devuelve UNO si el jugador UNO tiene mejor puntería. De lo contrario, devuelve DOS.
    """

    res:Jugador

    punteriaJugadorUno:int = punteríaDeJugador(estadoDeJuego, UNO)
    punteriaJugadorDos:int = punteríaDeJugador(estadoDeJuego, DOS)

    if punteriaJugadorUno>punteriaJugadorDos:
        res = UNO
    else:
        res = DOS

    return res

def cantidadDePosicionesConAgua(grilla:Grilla)->int:

    res:int = 0

    for fila in grilla:

        for posicion in fila:

            if posicion == AGUA:
                res += 1

    return res

def barcoDescubiertoEn (barco:BarcoEnGrilla, grilla:Grilla)->bool:
    
    for posicion in barco:
        if celdaEnPosición(grilla,posicion) != VACÍO:
            return True
    
    return False

def cantidadDeBarcosDescubiertos(estadoDeJuego:EstadoJuego, jugador:Jugador)->int:

    res:int = 0

    jugadorOponente:Jugador = jugadorOpuesto(jugador)

    barcosOponente:list[list[BarcoEnGrilla]] = barcosEnGrilla(tableroDeJugador(estadoDeJuego, jugadorOponente)[0])

    grillaOponenteLocal:Grilla = grillaOponente(tableroDeJugador(estadoDeJuego, jugador))

    for barco in barcosOponente:
        if barcoDescubiertoEn(barco, grillaOponenteLocal):
            res += 1

    return res

def jugadorOpuesto(jugador:Jugador)->Jugador:

    if jugador == UNO:
        return DOS
    else:
        return UNO     

def punteríaDeJugador(estadoDeJuego:EstadoJuego,jugador:Jugador)->int:
    res:int
    grilla_Oponente:Grilla = grillaOponente(tableroDeJugador(estadoDeJuego, jugador))
    res = cantidadDeBarcosDescubiertos(estadoDeJuego, jugador) - cantidadDePosicionesConAgua(grilla_Oponente)

    return res