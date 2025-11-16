from queue import Queue as Cola

#Ejercicio 1

def cantidad_subsecuencias_que_suman(s: list[int], n: int) -> int:

	subsecuenciasPosibles:list[list[int]] = armarTodasLasSubsecs(s)
	contador:int = 0

	for subsec in subsecuenciasPosibles:
		if len(subsec) != 0 and sumaEsN(subsec, n):
			contador = contador +1

	return contador 


def armarTodasLasSubsecs(l:list[int])->list[list[int]]:

	desde:int = len(l) -1
	hasta:int = 0 #el índice 0 de la lista, ya que en la función armarSubsecDesdeHasta le voy a restar 1
	res:list[list[int]] = []
	for i in range (desde, hasta-1,-1):

		for j in range (desde, hasta-1,-1):

			subsec:list[int] = armarSubsecDesdeHasta(l,i,j)
			res.append(subsec)
	
	return res


def armarSubsecDesdeHasta(l:list[int], n:int, m:int)->list[int]:
	lista:list[int] = []
	for i in range (n, m-1, -1):
		lista.append(l[i])

	return lista


def sumaEsN(numeros:list[int], n:int)->bool:
	
	return sumarLista(numeros) == n

def sumarLista(numeros:list[int])->int:
	res:int = 0
	for numero in numeros:
		res = res + numero
	
	return res

#Ejercicio 2

def abrir_caja_prioridad(clientes: Cola[tuple[str, bool]]) -> Cola[str]:
    
	clientesPrioritarios:Cola[str] = Cola()
	clientesAux:Cola[tuple[str,bool]] = Cola()

	while not clientes.empty():
		
		cliente:tuple[str,bool] = clientes.get()

		if clienteEsPrioritario(cliente):
			clientesPrioritarios.put(cliente[0])
		else:
			clientesAux.put(cliente)

	while not clientesAux.empty():
		clientes.put(clientesAux.get())

	return clientesPrioritarios


def clienteEsPrioritario(cliente:tuple[str,bool])->bool:

	return cliente[1] 

#Ejercicio 3

def buscar_columna_con_maximo_menor_a_cota(A: list[list[int]], cota: int) -> int:
	cantFilas:int = len(A)
	cantColumnas:int = len(A[0])
	max:int
	columnaRes:int

	seAccedioAlPrimerElemento:bool = False
	
	for i in range (0, cantFilas, 1):

		for j in range (0, cantColumnas, 1):

			if not seAccedioAlPrimerElemento:
				seAccedioAlPrimerElemento =True
				max = A[i][j]
				columnaRes = j
			else:
				elemento:int = A[i][j]
				if elementoCumpleCondiciones(elemento, cota, max) and j<len(A[0]):
					max = elemento
					columnaRes = j

	return columnaRes

def elementoCumpleCondiciones(n:int, cota:int, max:int):
	return compararElementoConCota(n,cota) and compararDosElementos(n,max) and n>=0


def compararElementoConCota(n:int, cota:int)->bool:
	return n < cota

def compararDosElementos(n:int, m:int)->bool:
	return n>m

#Ejercicio 4

def agrupar_por_autor_con_cota(libros: dict[str, str], cota: int) -> dict[str, list[str]]:
	
	autoresChequeados:list[str] = []
	listaDeRes:list[tuple[str,list[str]]] = []
	res:dict[str, list[str]] = {}
	
	for item in libros.items():

		parLibroAutor:tuple[str,str] = item
		autor:str = parLibroAutor[1]

		if parLibroAutor[1] not in autoresChequeados and autorApareceNOMasVeces(libros, autor, cota):
			tuplaAutorLibros:tuple[str,list[str]] = crearTuplaAutorLibros(libros, autor)
			listaDeRes.append(tuplaAutorLibros)
			autoresChequeados.append(autor)
		else:
			autoresChequeados.append(autor)

	res = crearDiccionario(listaDeRes)

	return res
	
		
def crearDiccionario(listaAutorLibros:list[tuple[str, list[str]]])->dict[str,list[str]]:

	res:dict[str,list[str]] = {}

	for elemento in listaAutorLibros:
		autor:str = elemento[0]
		libros:list[str] = elemento[1]

		res[autor] = libros

	return res


def crearTuplaAutorLibros(libros:dict[str,str], autor:str)->tuple[str, list[str]]:

	res:tuple[str,list[str]] = ()
	librosDelAutor:list[str] = []

	for item in libros.items():
		par:tuple[str,str] = item

		if par[1] == autor:
			librosDelAutor.append(par[0])

	res = (autor, librosDelAutor)
	return res


def autorApareceNOMasVeces(libros:dict[str,str], autor:str, n:int)->bool:

	autores:list[str] = libros.values()
	res:int
	
	res = contarAparicionesDeElm(autores, autor)

	return res >= n
		

def contarAparicionesDeElm(lista:list[str], elm:str )->int:

	apariciones:int = 0

	for item in lista:
		if item == elm:
			apariciones = apariciones +1
	
	return apariciones
