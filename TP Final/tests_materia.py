import unittest
from batallaNaval import *

# Tests
# Tests Ejercicio 1

class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): # Un ejemplo de test 
        barcos = [[('H',3), ('H',4), ('H',5)],
                [('F',4), ('E',4)],
                [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                [('F',4), ('E',4)],
                                [('B',4), ('B',3), ('B',2)]] )
        
    def test_mas_de_un_barco_de_un_tamaño(self):
        barcos = [[('H',3), ('H',4), ('H',5)],
                [('F',4), ('E',4)],
                [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,3),2)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                [('F',4), ('E',4)],
                                [('B',4), ('B',3), ('B',2)]] )
        
    def test_no_hay_barcos_de_tamaño(self):
        barcos = [[('H',3), ('H',4), ('H',5)],
                [('F',4), ('E',4)],
                [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,4),0)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                [('F',4), ('E',4)],
                                [('B',4), ('B',3), ('B',2)]])
        
#test ejercicio 2 

class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self): #
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        self.assertEqual(juego[0], (2,2))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_sin_barcos(self):
            
        juego = nuevoJuego(1, 1, [])
        self.assertEqual(juego[0], (1, 1))
        self.assertEqual(juego[1], [])
        self.assertEqual(juego[2], [UNO])

    def test_26x1_y_un_barco_longitud_1(self):

        grillaUNO_local = [[VACÍO] for _ in range(26)]
        grillaUNO_oponente = [[VACÍO] for _ in range(26)]
        grillaDOS_local = [[VACÍO] for _ in range(26)]
        grillaDOS_oponente = [[VACÍO] for _ in range(26)]


        juego = nuevoJuego(26,1,[1])
        self.assertEqual(juego[0], (26,1))
        self.assertTrue(juego[1], [1])
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))


# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_Columnas_vacías (self): #las grillas tienen filas vacías
        grillaUnoLocal:Grilla = [[]]
        
        grillaUnoOponente:Grilla= [[]]
        
        grillaDosLocal:Grilla = [[]]
        
        grillaDosOponente:Grilla = [[]]

        estadoJuego:EstadoJuego = ((1,1), [0,0], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estadoJuego))
        self.assertEqual(estadoJuego,((1,1), [0,0], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))


    def test_cantidad_no_coinciden_filas_de_los_tableros(self): #El tablero del jugador UNO es de 5x5 pero el del jugador DOS es de 4x4
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estadoDeJuego = ((5,5), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estadoDeJuego))
        self.assertEqual(estadoDeJuego,((5,5), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)) )

    def test_hay_mas_de_un_turno_activo(self): #la longitud de estado[2] es mayor que 1 (es 2)
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[BARCO, BARCO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estadoJuego = ((4,4), [2,2], [DOS,UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estadoJuego))        
        self.assertEqual(estadoJuego, ((4,4), [2,2], [DOS,UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
    
    def test_no_coinciden_posiciones_atacadas(self): #Hay una posición atacada en la grilla oponente del jugador uno que no se ve reflejada en la grilla local del jugador dos
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, AGUA],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, TOCADO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[BARCO, BARCO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, AGUA],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estadoJuego = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estadoJuego))
        self.assertEqual(estadoJuego, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_coinciden_posiciones_atacadas_dos(self): 
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, AGUA],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[BARCO, BARCO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[TOCADO, VACÍO, VACÍO, AGUA],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estadoJuego = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estadoJuego))
        self.assertEqual(estadoJuego, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))


    def test_hay_más_de_26_filas(self): #el tablero 27 filas y 4 columnas. Tampoco tiene barcos, aunque se marquen como disponibles 2

        grillaUnoLocal:Grilla = []
        grillaUnoOponente:Grilla = []
        grillaDosLocal:Grilla = []
        grillaDosOponente:Grilla = []

        for _ in range(28):

            fila = []

            for _ in range(4):

                fila.append(VACÍO)

            grillaUnoLocal.append(fila.copy())
            grillaUnoOponente.append(fila.copy())
            grillaDosLocal.append(fila.copy())
            grillaDosOponente.append(fila.copy())
        
        estadoJuego:EstadoJuego = ((27,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estadoJuego))
        self.assertEqual(estadoJuego,((27,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)) )

        
    def test_esta_todo_más_que_bien (self): #el estado es válido

        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estadoJuego:EstadoJuego = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estadoJuego))
        self.assertEqual(estadoJuego, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_difieren_barcos_en_Grilla(self):
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_lleno_de_barcos(self):
        grillaUnoLocal = [[BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO]]
        
        grillaUnoOponente = [[BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO]]
        
        grillaDosLocal = [[BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO]]
        
        grillaDosOponente = [[BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO],
                          [BARCO, BARCO, BARCO, BARCO]]
        
        estado = ((4,4), [4,4], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [4,4], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))


    def test_todo_vacío(self):
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [0,0], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))      
        self.assertTrue(compararPosicionDeTablero(tableroDeJugador(estado, UNO),tableroDeJugador(estado, DOS)))  
        self.assertEqual(estado, ((4,4), [0,0], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_celdas_no_vacias_iguales_compararPosicionDeTablero(self):

        grillaUnoLocal = [[BARCO, VACÍO],
                        [VACÍO, VACÍO]]
        
        grillaUnoOponente = [[BARCO, VACÍO],
                            [VACÍO, VACÍO]]
        
        grillaDosLocal = [[BARCO, VACÍO],
                        [VACÍO, VACÍO]]
        
        grillaDosOponente = [[BARCO, VACÍO],
                            [VACÍO, VACÍO]]

        estadoJuego = ((2,2), [1,1], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(compararPosicionDeTablero(tableroDeJugador(estadoJuego, UNO),tableroDeJugador(estadoJuego, DOS)))

    def test_cantPosicionesNoVacias_todo_vacio(self):
        grillaUnoLocal = [[VACÍO, VACÍO],
                        [VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO],
                            [VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO],
                        [VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO],
                            [VACÍO, VACÍO]]

        estadoJuego = ((2,2), [0,0], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertEqual(cantPosicionesNoVacias(grillaLocal(tableroDeJugador(estadoJuego, UNO))), 0)
        self.assertEqual(cantPosicionesNoVacias(grillaOponente(tableroDeJugador(estadoJuego, DOS))), 0)
        
# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparar_en_barco(self):
        estado:EstadoJuego = ((3, 3), [2, 2], [UNO],
            (
                [[BARCO, BARCO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ),
            (
                [[BARCO, VACÍO, VACÍO],
                 [BARCO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ))

        estado_esperado:EstadoJuego = ((3, 3), [2, 2], [DOS],
            (
                [[BARCO, BARCO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]],
                [[BARCO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ),
            (
                [[BARCO, VACÍO, VACÍO],
                 [BARCO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ))

        resultado:ResultadoDisparo = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)
    
    def test_turno_cambia_despues_disparo(self):
        estado = ((2, 2), [1, 1], [UNO],
            (
                [[VACÍO, VACÍO], [VACÍO, VACÍO]],
                [[VACÍO, VACÍO], [VACÍO, VACÍO]]
            ),
            (
                [[VACÍO, VACÍO], [VACÍO, VACÍO]],
                [[VACÍO, VACÍO], [VACÍO, VACÍO]]
            ))
        #Esta variable no se usa directamente ya que lo que estoy buscando en este caso de test es que cambie el estado puntualmente en el turno
        resultado:ResultadoDisparo = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(turno(estado), DOS)

    def test_disparo_al_borde_de_grilla(self):
        estado:EstadoJuego = ((3, 3), [1, 1], [UNO],
            (
                [[VACÍO, BARCO, VACÍO] ,
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]],
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ),
            (
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, BARCO]],
                [[VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO],
                 [VACÍO, VACÍO, VACÍO]]
            ))
        resultado:ResultadoDisparo = dispararEnPosición(estado, ("C", 3))
        self.assertEqual(resultado, TOCADO)

    def test_disparo_turno_dos_en_barco(self):
        estado = ((2, 2), [1, 1], [DOS],
            (
                [[VACÍO, VACÍO],
                [BARCO, VACÍO]],
                [[VACÍO, VACÍO],
                [VACÍO, VACÍO]]
            ),
            (
                [[BARCO, VACÍO],
                [VACÍO, VACÍO]],
                [[VACÍO, VACÍO],
                [VACÍO, VACÍO]]
            ))

        estado_esperado = ((2, 2), [1, 1], [UNO],
            (
                [[AGUA, VACÍO],
                [BARCO, VACÍO]],
                [[VACÍO, VACÍO],
                [VACÍO, VACÍO]]
            ),
            (
                [[BARCO, VACÍO],
                [VACÍO, VACÍO]],
                [[AGUA, VACÍO],
                [VACÍO, VACÍO]]
            ))

        resultado: ResultadoDisparo = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)


# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                        [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('D',3), ('D',4)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])
        
    def test_varios_barcos_verticales(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('D',6), ('E',6)],
                                                [('D',1), ('C',1), ('D',1)],
                                                [('D',4),('C',4), ('B',4)]]
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                        [BARCO, VACÍO, VACÍO, BARCO, VACÍO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])
        
    def test_varios_barcos_horizontales(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, BARCO, BARCO, BARCO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('B',1), ('B',2), ('B',3), ('B',4)],
                                                [('D',4),('D',5), ('D',6)]]
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [BARCO, BARCO, BARCO, BARCO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])

    def test_sin_barcos(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = []
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertFalse(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])

#Tests ejercicio 6

class elJugadorConMejorPuntería_Test(unittest.TestCase):
    def test_gana_DOS(self):
        grillaUnoLocal = [[BARCO, BARCO],
                        [VACÍO, VACÍO]]
        
        grillaUnoOponente = [[AGUA, AGUA],
                            [VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO],
                        [BARCO, BARCO ]]
        
        grillaDosOponente = [[BARCO, AGUA],
                            [VACÍO, VACÍO]]

        estadoJuego = ((2,2), [1,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertEqual(elJugadorConMejorPuntería(estadoJuego), DOS)
    
    def test_gana_uno(self):
        grillaUnoLocal = [[BARCO, VACÍO, BARCO],
                        [BARCO, VACÍO, BARCO],
                        [VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[BARCO, VACÍO, VACÍO],
                        [VACÍO, VACÍO, VACÍO],
                        [VACÍO, BARCO, VACÍO]]
        
        grillaDosLocal = [[BARCO, BARCO, VACÍO],
                        [VACÍO, VACÍO, VACÍO],
                        [VACÍO, BARCO, BARCO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, BARCO],
                        [VACÍO, VACÍO, BARCO],
                        [VACÍO, VACÍO, VACÍO]]

        estadoJuego = ((3,3), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertEqual(elJugadorConMejorPuntería(estadoJuego), UNO)

if __name__ == '__main__':
    unittest.main(verbosity=1)
