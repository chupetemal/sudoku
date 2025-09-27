from Sudoku import CrearSudoku
def main():
    Sudoku=[]
    while len(Sudoku)!=1:
        Sudoku.append(CrearSudoku(Sudoku))
        print(Sudoku)


if __name__ == "__main__":
    main()