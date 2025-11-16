{--
Yo: Facundo David Rabago
Certifico que el siguiente archivo fue elaborado únicamente por mí, sin ayuda de otras personas o herramientas.
--}

module SolucionT1 where

-- Ejercicio 1
esCuadradoDePrimo :: Integer -> Bool
esCuadradoDePrimo numero = verificarSiExistePRequerido numero (formarListaNaM 2 numero)


formarListaNaM :: Integer->Integer->[Integer]
formarListaNaM n m | n == m = [n]
                   | otherwise = n : formarListaNaM (n+1) m 

verificarSiExistePRequerido :: Integer->[Integer]->Bool
verificarSiExistePRequerido _ [] = False
verificarSiExistePRequerido num (x:xs) | esPrimo x && num == x^2 = True
                                       | otherwise = verificarSiExistePRequerido num xs

divisores :: Integer->[Integer]->[Integer]
divisores n [] = []
divisores n (x:xs) | mod n x == 0 = x : divisores n xs
                   | otherwise = divisores n xs  
longitudLista :: [Integer]->Integer
longitudLista [] = 0
longitudLista (x:xs) = 1 + longitudLista xs 

esPrimo :: Integer->Bool
esPrimo n = longitudLista (divisores n (formarListaNaM 1 n)) == 2

-- Ejercicio 2
posParesFormanEscalera :: [Integer] -> Bool
posParesFormanEscalera [a,b] = True -- si me quedan sólo dos elementos no importa si queda algún par, ya que no van a cumplir la condición "par i tal que 0 ≤ i < |lista|-2"
posParesFormanEscalera (x:xs) | not (esPar x) = True && posParesFormanEscalera xs
                              | otherwise = x >= 0 && (x+1) == head(tail xs)      

esPar :: Integer->Bool
esPar n = mod n 2 == 0


-- Ejercicio 3
listadoDePeliculas :: [(Integer, [String])] -> [(String, Integer)]
listadoDePeliculas [] = []
listadoDePeliculas ((anio,[]):resto) = listadoDePeliculas resto
listadoDePeliculas ((anio, (pelicula:restoMismoAnio)):resto) = (pelicula,anio) : listadoDePeliculas ((anio,(restoMismoAnio)):resto)


-- Ejercicio 4
eliminarFilaQueMasSuma :: [[Integer]] -> [[Integer]]
eliminarFilaQueMasSuma [a] = []
eliminarFilaQueMasSuma (fila:resto) | sumarFila fila >= sumarFila (head resto) = (head resto) : eliminarFilaQueMasSuma (fila:tail resto)
                                    | otherwise = fila : eliminarFilaQueMasSuma resto

sumarFila :: [Integer]->Integer
sumarFila [] = 0
sumarFila (x:xs) = x + sumarFila xs

{--
Siendo la última modificación con la solución final:
01/10/25 11:19
--}
