def main():
    adapters = [0]  # Start with zero for wall
    with open("input.txt") as adapter_input:
        for line in adapter_input:
            adapters.append(int(line.rstrip()))
    adapters.sort()
    adapters.append(adapters[-1] + 3)  # Add phone adapter, +3 of max

    one_count = 0
    three_count = 0
    in_a_row = 0  # Keeps track of the number of 1 jumps in a row
    arrangements = 1  # Total arrangements product of all 1 jolt sequences

    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] == 1:
            in_a_row += 1
            one_count += 1
        elif adapters[i + 1] - adapters[i] == 3:
            if in_a_row == 2:  # Two 1 jolt jumps in a row = 2 arrangements
                arrangements *= 2
            elif in_a_row == 3:  # Three 1 jolt jumps = 4 arrangements
                arrangements *= 4
            elif in_a_row == 4:  # Four 1 jolt jumps = 7 arrangements
                arrangements *= 7  # I found these numbers by manually going through each possibility
            in_a_row = 0
            three_count += 1
    print("Product of one and three volt jump counts: {}".format(one_count * three_count))
    print("Total number of arrangements: {}".format(arrangements))


if __name__ == "__main__":
    main()
