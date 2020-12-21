def main():

    with open("input.txt") as shuttle_data:
        earliest_timestamp = int(shuttle_data.readline().rstrip())
        shuttles = shuttle_data.readline().rstrip().split(',')

    record = ()
    for shuttle in shuttles:
        if shuttle == 'x':
            continue

        shuttle = int(shuttle)
        time = 0
        while time < earliest_timestamp:
            time += shuttle
        time_over = time - earliest_timestamp
        if record == ():
            record = (shuttle, time_over)
        elif time_over < record[1]:
            record = (shuttle, time_over)

    print(record[0] * record[1])


if __name__ == '__main__':
    main()