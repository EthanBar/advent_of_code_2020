def check_tree_hits(biome, row_skips, column_skips):
    row = 0
    column = 0
    tree_hit_count = 0

    while row < len(biome):
        if biome[row][column % len(biome[0])] == '#':
            tree_hit_count += 1
        column += column_skips
        row += row_skips

    return tree_hit_count


def main():
    biome = []
    with open("input.txt") as biome_data:
        row = 0
        for line in biome_data:
            biome.append([])
            for char in line.rstrip():  # rstrip to clear newlines
                biome[row].append(char)
            row += 1

    tree_counts = [check_tree_hits(biome, 1, 1), check_tree_hits(biome, 1, 3), check_tree_hits(biome, 1, 5),
                   check_tree_hits(biome, 1, 7), check_tree_hits(biome, 2, 1)]

    tree_count_multi = 1
    for count in tree_counts:
        tree_count_multi *= count

    print("Trees hit multiplied: {}".format(tree_count_multi))


if __name__ == "__main__":
    main()
