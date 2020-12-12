day5data = open("day5data.txt").read().split()
default_rows = []
default_columns = []
seat_id_list = []


def rowfinder(char: str, rows: list) -> list:
    new_rows = []
    if char == "B":
        if int(len(rows)) <= 2:
            new_rows = rows[1]
        else:
            row_min = int(len(rows)/2)
            row_max = int(len(rows))
            new_rows = rows[row_min:row_max]
    if char == "F":
        if int(len(rows)) <= 2:
            new_rows = rows[0]
        else:
            row_max = int(len(rows)/2)
            new_rows = rows[0:row_max]
    return new_rows


def columnfinder(char: str, columns: list) -> list:
    new_columns = []
    if char == "R":
        if int(len(columns)) <= 2:
            new_columns = columns[1]
        else:
            column_min = int(len(columns)/2)
            column_max = int(len(columns))
            new_columns = columns[column_min:column_max]
    if char == "L":
        if int(len(columns)) <= 2:
            new_columns = columns[0]
        else:
            column_max = int(len(columns)/2)
            new_columns = columns[0:column_max]
    return new_columns


# make the row array
for i in range(0, 128):
    default_rows.append(i)

# make the column array
for i in range(0, 8):
    default_columns.append(i)

for line in day5data:
    rows = default_rows
    columns = default_columns
    calc_row = []
    for char in line[0:7]:
        rows = rowfinder(char, rows)
    for char in line[7:]:
        columns = columnfinder(char, columns)
    seat_id = 8 * rows + columns
    seat_id_list.append(seat_id)

# part 1

# print(sorted(seat_id_list))

# part 2

previous_id = sorted(seat_id_list)[0] - 1
for id in sorted(seat_id_list):
    if id - previous_id == 1:
        previous_id = id
    else:
        print(previous_id, id)
        break

