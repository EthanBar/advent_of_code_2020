numbers = []
with open("totals.txt") as accounting:
    for line in accounting:
        numbers.append(int(line))

for n1 in numbers:
    for n2 in numbers:
        if n1 + n2 == 2020:
            print("Found it: {} + {} = 2020".format(n1, n2))
            print("Multiplied: {}".format(n1 * n2))
