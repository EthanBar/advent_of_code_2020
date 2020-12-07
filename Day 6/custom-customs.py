def main():
    groups = []
    with open("input.txt") as group_data:
        group = []
        for line in group_data:
            if line == "\n":
                groups.append(group)
                group = []
            else:
                person = set()
                for char in line.rstrip():
                    person.add(char)
                group.append(person)

        groups.append(group)

    total_yeses = 0

    for group in groups:
        total_yeses += len(set.intersection(*group))

    print("Total yeses: {}".format(total_yeses))


if __name__ == "__main__":
    main()