def get_seat_id(seat):
    # First time working with a binary structure here...no idea how gross this is
    count = 64
    row = 128
    for i in range(7):
        if seat[i] == 'F':
            row -= count
        count /= 2
    row -= 1

    count = 4
    column = 8
    for i in range(3):
        if seat[i + 7] == 'L':
            column -= count
        count /= 2
    column -= 1

    row = int(row)
    column = int(column)

    return row * 8 + column  # Seat ID formula


def main():
    # Organize data
    seats = []
    with open("input.txt") as boarding_data:
        for line in boarding_data:
            seats.append(line.rstrip())

    # Get all seat IDs
    seat_ids = []
    for seat in seats:
        seat_ids.append(get_seat_id(seat))
    seat_ids.sort()

    # Go through the sorted seat IDS and find the point where they aren't concurrent
    last = seat_ids[0]
    for seat in seat_ids[1:]:
        if last + 1 != seat:
            print("Your seat is: {}".format(last + 1))
            return
        last = seat


if __name__ == "__main__":
    main()
