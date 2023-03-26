"""
board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]

A1,A2,A3    00,01,02
B1,B2,B3    10,11,12
C1,C2,C3    20,21,22
"""
    
    
column_to_index = {'A':0, 'B':1, 'C':2}


def main():
    print(get_row_col("A3"))


def get_row_col(square):
    column, row = square[0], int(square[1])
    
    column_index = column_to_index[column]
    row_index = row - 1
    
    return (row_index, column_index)
    

main()
