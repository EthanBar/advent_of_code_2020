import copy


def find_accumulator_after_loop_or_terminate(instructions):
    accumulator = 0  # The value of the accumulator
    line = 0  # Which line is being read from
    visited_lines = set()  # Set of lines we have visited to avoid loops

    while True:
        visited_lines.add(line)
        if instructions[line]["code"] == 'acc':
            accumulator += instructions[line]["value"]
            line += 1
        elif instructions[line]["code"] == 'jmp':
            line += instructions[line]["value"]
        else:
            line += 1

        if line in visited_lines:
            return accumulator, "looped"  # Infinite loop found
        if line >= len(instructions):
            return accumulator, "terminated"  # Reached end of instructions


def main():
    instructions = []
    with open("input.txt") as instruction_data:
        for line in instruction_data:
            instructions.append({"code": line[:3], "value": int(line[4:].rstrip())})

    print("Value in accumulator when looped: {}".format(find_accumulator_after_loop_or_terminate(instructions)[0]))

    for i in range(len(instructions)):
        # We have to take a deep copy here as the dictionaries are still pointed to the same reference with .copy()
        instructions_copy = copy.deepcopy(instructions)
        # Alter the code
        if instructions_copy[i]["code"] == 'jmp':
            instructions_copy[i]["code"] = 'nop'
        elif instructions_copy[i]["code"] == 'nop':
            instructions_copy[i]["code"] = 'jmp'
        else:
            continue

        results = find_accumulator_after_loop_or_terminate(instructions_copy)
        if results[1] == "terminated":
            print("Value in accumulator when terminated: {}".format(results[0]))
            break


if __name__ == "__main__":
    main()
