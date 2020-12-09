def does_bag_contain(bag_rules, bag, search):
    if bag == search:  # Found the bag
        return True

    if bag is None:  # Dead end
        return False

    for content in bag_rules[bag]:
        if does_bag_contain(bag_rules, content["color"], search):
            return True
    return False  # No chance


def count_children_bags(bag_rules, bag, number):
    if bag is None:
        return 0

    total = 1

    for content in bag_rules[bag]:
        total += count_children_bags(bag_rules, content["color"], content["quantity"])
    return total * number


def main():
    bag_rules = {}  # Dictionary of all bags {"bag color" : [contents]}
    with open("input.txt") as bag_data:
        for line in bag_data:
            split = line.split(" bags ")

            contents = split[1][8:-2].replace(" bags", "").replace(" bag", "")
            bag_color = split[0]

            if contents == "no other":
                bag_rules[bag_color] = []
            else:
                bag_rules[bag_color] = []
                for item in contents.split(", "):
                    content = {"color": item.split(" ", 1)[1:][0], "quantity": int(item.split()[:1][0])}
                    bag_rules[bag_color].append(content)

    shiny_found = 0
    for bag in bag_rules.keys():
        if does_bag_contain(bag_rules, bag, "shiny gold"):
            shiny_found += 1

    print("Bags that contain a shiny gold bag: {}".format(shiny_found - 1))
    print("Bags inside a shiny gold bag: {}".format(count_children_bags(bag_rules, "shiny gold", 1) - 1))


if __name__ == "__main__":
    main()
