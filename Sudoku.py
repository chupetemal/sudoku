import random
def CrearSudoku(Sudoku):   
    CubosSudoku=[]
    CubosSudoku=[[random.randint(1,9)for i in range(3)]for i in range(3)]
    CubosSudoku=RevisarRepetidos(CubosSudoku)

    print("esto es lo q se devolvio",CubosSudoku)
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
    print("entro la bala")
    Repetidos=[]
    NumerosFaltantes=[]
    print(Cubos)
    print(Cubos[0])
    for i in range(1,10):
        Contador=0
        Veces=0
        for j in range(len(Cubos)):
            for l in range(len(Cubos[0])):
                print(i)
                if i == Cubos[j][l]:
                    Contador+=1
                    
                    if i not in Cubos[l] and l == j:
                        Veces+=1
                        if Veces==3:
                            NumerosFaltantes.append(i)
                            
                    
                        
                    
            if Contador>1:
                print("el numero",i,"esta en la lista",Contador,"veces")
                Repetidos.append(i)
                print("re",Repetidos)
    
    print("nym",NumerosFaltantes)
    if len(Repetidos)>0 or len(NumerosFaltantes)>0:
        SacarRepetidos(Cubos,Repetidos,NumerosFaltantes)
    else:
        print("esta lista esta completa")
        print(Cubos)
        return (Cubos)


def SacarRepetidos(Cubos,Repetidos,NumerosFaltantes):
    while True:
        print(Repetidos)
        if NumerosFaltantes==0:
            break
        else:
            NumerosFaltantes.remove()
            print(NumerosFaltantes)

    
    RevisarRepetidos(Cubos)

