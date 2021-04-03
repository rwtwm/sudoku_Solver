def correct():
    writefile = open(r'D:\Documents\01 Python\0110 SudokuSolver\sudoku_Solver\Text\SampleGridCorr.txt', 'w')
    with open(r'D:\Documents\01 Python\0110 SudokuSolver\sudoku_Solver\Text\SampleGrid.txt', 'r') as file:
        for line in file.readlines():
            x, y, z = line.split(',')
            x, y, z = y, x, z
            writeStr = x + ',' + y + ',' + z
            writefile.write(writeStr)


if __name__ == "__main__":
    correct()
