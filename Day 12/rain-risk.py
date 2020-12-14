cardinals = {'N': 0, 'E': 90, 'S': 180, 'W': 270}


def main():
    directions = []
    with open("input.txt") as direction_data:
        for line in direction_data:
            direction = (line[0], int(line.rstrip()[1:]))  # [Instruction, Amount]
            directions.append(direction)

    coordinate = [0, 0]  # Coordinate keeps track of ships location
    degrees = 90  # Part 1 uses degrees to keep track of ship's headings

    for direction in directions:
        if direction[0] == 'L':
            degrees -= direction[1]
            continue
        elif direction[0] == 'R':
            degrees += direction[1]
            continue
        elif direction[0] == 'F':
            heading = degrees % 360  # Modulo will make the math easier
        else:
            heading = cardinals[direction[0]]  # If N, S, E or W find the associated heading

        if heading == 0:
            coordinate[0] += direction[1]
        elif heading == 90:
            coordinate[1] += direction[1]
        elif heading == 180:
            coordinate[0] -= direction[1]
        elif heading == 270:
            coordinate[1] -= direction[1]

    print("Part 1 Manhattan distance: {}".format(abs(coordinate[0]) + abs(coordinate[1])))

    coordinate = [0, 0]  # Reset the coordinates
    waypoint = [1, 10]  # Part 2 uses a waypoint, is always relative to ship's coordinate

    for direction in directions:
        if direction[0] == 'L' or direction[0] == 'R':
            if direction[1] == 180:  # Flip around 180
                waypoint = [-waypoint[0], -waypoint[1]]
            elif direction[0] == 'L' and direction[1] == 90 or direction[0] == 'R' and direction[1] == 270:
                # 270 degrees clockwise
                waypoint = [waypoint[1], -waypoint[0]]
            else:
                waypoint = [-waypoint[1], waypoint[0]]  # 90 degrees clockwise
        elif direction[0] == 'F':
            for _ in range(direction[1]):  # Move ship towards relative waypoint _ times
                coordinate[0] += waypoint[0]
                coordinate[1] += waypoint[1]
        elif direction[0] == 'N':
            waypoint[0] += direction[1]
        elif direction[0] == 'S':
            waypoint[0] -= direction[1]
        elif direction[0] == 'E':
            waypoint[1] += direction[1]
        elif direction[0] == 'W':
            waypoint[1] -= direction[1]

    print("Part 2 Manhattan distance: {}".format(abs(coordinate[0]) + abs(coordinate[1])))


if __name__ == "__main__":
    main()
