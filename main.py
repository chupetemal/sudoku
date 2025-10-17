from Sudoku import CrearSudoku, MostrarSudoku,JugarAlJogo
def main():
    print("1.hacer un sudoku")
    print("2.resolver un sudoku")    
    Seleccion=int(input("ingrese el numero de la opcion que desea seleccionar: "))
    while  Seleccion < 1 or Seleccion > 2:
        Seleccion=int(input("ingrese el numero de la opcion que desea seleccionar: "))
    
    if Seleccion == 1:
        Sudoku=[]
        while len(Sudoku)!=9:
            Sudoku.append(CrearSudoku(Sudoku))
        MostrarSudoku(Sudoku)

    else:
        Sudoku=[]
        while len(Sudoku)!=9:
            Sudoku.append(CrearSudoku(Sudoku))
        
        


if __name__ == "__main__":
    main()