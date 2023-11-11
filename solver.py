import csv
from helpers import get_columns, get_rows, get_squares


class Sudoku:
    def __init__(self,reader: list):
        self.columns = get_columns(reader)
        self.rows = get_rows(reader)
        self.squares = get_squares(reader)

if __name__ == '__main__':

    with open('e.csv', newline='') as f:
        reader = csv.reader(f)
        reader = list(reader)
    sudoku = Sudoku(reader)










