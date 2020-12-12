directions = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]


def check_seat(seating, row, column, row_march, column_march, use_sight):
    # This loop checks that indices won't go out of bounds
    while 0 <= row + row_march < len(seating) and 0 <= column + column_march < len(seating[0]):
        row += row_march
        column += column_march
        if seating[row][column] == '#':
            return True
        if seating[row][column] == 'L' or not use_sight:
            return False
    return False


def get_occupied_neighbors(seating, row, column, use_sight):
    occupied_count = 0
    for direction in directions:  # Check all 8 directions for occupied seats
        if check_seat(seating, row, column, direction[0], direction[1], use_sight):
            occupied_count += 1
    return occupied_count


def run_update(seating, tolerance, use_sight):
    new_seating = []
    for row in range(len(seating)):
        new_row = []
        for column in range(len(seating[0])):
            seat_status = seating[row][column]
            occupied_neighbors = get_occupied_neighbors(seating, row, column, use_sight)
            if seat_status == 'L' and occupied_neighbors == 0:
                seat_status = '#'
            elif seat_status == '#' and occupied_neighbors >= tolerance:
                seat_status = 'L'
            new_row.append(seat_status)
        new_seating.append(new_row)
    return new_seating


def main():
    seating = []
    with open("input.txt") as seating_data:
        for line in seating_data:
            row = []
            for char in line.rstrip():
                row.append(char)
            seating.append(row)

    previous_seating = []
    while previous_seating != seating:
        previous_seating = seating
        seating = run_update(seating, 5, True)

    occupied_count = 0
    for row in seating:
        for seat in row:
            if seat == '#':
                occupied_count += 1

    print("Occupied seats: {}".format(occupied_count))


if __name__ == "__main__":
    main()
