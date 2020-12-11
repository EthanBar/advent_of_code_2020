def find_target(numbers):
    for i in range(24, len(numbers)):  # Walk each section of the list
        target = numbers[i]
        target_found = False
        for n1 in range(i - 25, i):  # Pick a first number...
            for n2 in range(i - 25, i):  # and pair it with a second
                if numbers[n1] + numbers[n2] == target and n1 != n2:  # Ensure it's not the same number
                    target_found = True
                    break

        if not target_found:
            return target


def find_sum(numbers, target):
    for step in range(2, len(numbers) - 1):  # Step is total size of numbers we are summing
        for offset in range(len(numbers) - step - 1):  # Offset is how far from the start we offset the sum
            summation = 0
            minimum = numbers[offset]  # Keep track of these for the answer
            maximum = numbers[offset]
            for n in range(step):
                found = numbers[n + offset]
                summation += found
                if found < minimum:
                    minimum = found
                if found > maximum:
                    maximum = found
            if summation == target:
                return minimum + maximum


def main():
    numbers = []
    with open("input.txt") as data:
        for line in data:
            numbers.append(int(line.rstrip()))

    target = find_target(numbers)
    print("The target is: {}".format(target))
    weakness = find_sum(numbers, target)
    print("The weakness is: {}".format(weakness))


if __name__ == "__main__":
    main()
