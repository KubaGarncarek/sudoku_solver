def get_columns(reader):
    columns = []
    for col_number in range(len(reader)):
        column = []
        for row in reader:
            column.append(row[col_number])
        columns.append(column)
    return columns 

def get_rows(reader):
    rows = []
    for row in reader:
        rows.append(row)
    return rows

def get_squares(reader):
    squares = []
    square = []
    num = 0
    for i in range(3):
        for row in reader:
            if num % 3 == 0 and num != 0:
                num = 0
                squares.append(square)
                square = []
            for y in range(3):
                square.append(row[y+3*i])
            num +=1
    squares.append(square)
    return squares




