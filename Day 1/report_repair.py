def main():
    numbers = []
    with open("input.txt") as accounting:
        for line in accounting:
            numbers.append(int(line))

    for n1 in numbers:
        for n2 in numbers:
            if n1 + n2 == 2020:
                print("Found it: {} + {} = 2020".format(n1, n2))
                print("Multiplied: {}".format(n1 * n2))

    for n1 in numbers:
        for n2 in numbers:
            for n3 in numbers:
                if n1 + n2 + n3 == 2020:
                    print("Found it: {} + {} + {} = 2020".format(n1, n2, n3))
                    print("Multiplied: {}".format(n1 * n2 * n3))


if __name__ == "__main__":
    main()