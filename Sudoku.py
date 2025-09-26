import random
def CrearSudoku(Sudoku):
    CubosSudoku=[[random.randint(1,9)for i in range(3)]for i in range(3)]
    RemoverRepetidos(CubosSudoku)
    print("creando")


def RemoverRepetidos(Cubos):
    Repetidos=[]
    NumerosFaltantes=[]
    print(Cubos)
    print(Cubos[0])
    for i in range(1,10):
        Contador=0
        Veces=0
        for j in range(len(Cubos)):
            for l in range(len(Cubos[0])):
                if i == Cubos[j][l]:
                    Contador+=1
                else:
                    if Veces==0:
                        Veces=1
                        NumerosFaltantes.append(i)
                        print(NumerosFaltantes)
                        
                    else:
                        continue
        if Contador>1:
                print("el numero",i,"esta en la lista",Contador,"veces")
                Repetidos.append(i)
                print(Repetidos)
