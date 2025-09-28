from Sudoku import CrearSudoku
def main():
    print("1.hacer un sudoku")
    print("2.resolver un sudoku")    
    Seleccion=int(input("ingrese el numero de la opcion que desea seleccionar: "))
    while  Seleccion < 1 or Seleccion > 2:
        Seleccion=int(input("ingrese el numero de la opcion que desea seleccionar: "))
    
    if Seleccion == 1:
        Sudoku=[]
        while len(Sudoku)!=3:
            Sudoku.append(CrearSudoku(Sudoku))
        print(Sudoku)
    else:
        print("proximamente")
        


if __name__ == "__main__":
    main()