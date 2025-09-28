import random
def CrearSudoku(Sudoku):   
    CubosSudoku = []
    CubosSudoku = [[random.randint(1,9)for i in range(3)]for i in range(3)]
    RevisarRepetidos(CubosSudoku)

    return CubosSudoku
    """
    #forma pussy(inteligente de hacer lo de abajo)
    ListaAux=[]
    while len(ListaAux)!=9:
        for i in range(3):
            for j in range(3):
                for l in range(3):
                    numero=random.randint(1,9)
                    if numero not in ListaAux:
                        ListaAux.append(numero)
                     
    for i in range(3):
        print(ListaAux)
        print(ListaAux[0+i:9:3])
        CubosSudoku.append(ListaAux[0+i:9:3])
        print(CubosSudoku)
    """

def RevisarRepetidos(Cubos):
    Repetidos = []
    NumerosFaltantes = []
    for i in range(1,10):
        Contador = 0
        Veces = 0
        for j in range(len(Cubos)):
            for l in range(len(Cubos[0])):
                if i == Cubos[j][l]:
                    Contador += 1
                if i not in Cubos[j] and l == j:
                    Veces += 1
                    if i not in NumerosFaltantes and Veces == 3:
                        NumerosFaltantes.append(i)
            
            if Contador > 1:
                if i not in Repetidos:
                    Repetidos.append(i)
                    
    if len(Repetidos) > 0 or len(NumerosFaltantes) > 0:
        SacarRepetidos(Cubos,Repetidos,NumerosFaltantes)
    else:
        return(Cubos)

def SacarRepetidos(Cubos,Repetidos,NumerosFaltantes):
    while True:
        if len(NumerosFaltantes) == 0:
            break

        elif len(Repetidos) == 0:
            break
    
        else:
            Numero=NumerosFaltantes[0]
            NumerosFaltantes.remove(Numero)
            while True:
                for i in range(len(Cubos)):
                    Cantidad = 0
                    Repetido = Repetidos[0]
                    
                    for j in range(len(Cubos)):   
                        Cantidad += Cubos[j].count(Repetido)
                    try:
                        ubicacion = Cubos[i].index(Repetido)
                    except ValueError:
                        continue
                    else:
                        if Cantidad > 1:
                            Cubos[i][ubicacion] = Numero

                else:
                    Repetidos.remove(Repetido)
                    break
    RevisarRepetidos(Cubos)           
            

