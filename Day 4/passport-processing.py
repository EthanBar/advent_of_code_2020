import re


def validate_passport(passport):
    if not passport.keys() >= {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}:
        return False

    if 1920 > int(passport["byr"]) or int(passport["byr"]) > 2002:
        return False
    if 2010 > int(passport["iyr"]) or int(passport["iyr"]) > 2020:
        return False
    if 2020 > int(passport["eyr"]) or int(passport["eyr"]) > 2030:
        return False

    if passport["hgt"][-2:] == "cm":
        if 150 > int(passport["hgt"][:-2]) or int(passport["hgt"][:-2]) > 193:
            return False
    else:
        if 59 > int(passport["hgt"][:-2]) or int(passport["hgt"][:-2]) > 76:
            return False

    if not re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
        return False
    if not re.match(r"^[0-9]{9}$", passport["pid"]):
        return False

    return passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def main():
    # Organizing the passport data
    passports = []
    with open("input.txt") as passport_data:
        passport = {}
        for line in passport_data:
            if line == "\n":
                passports.append(passport)
                passport = {}
            else:
                i = 0
                selector = ""
                for part in line.replace(' ', ':').split(":"):
                    if i % 2 == 0:
                        selector = part
                    else:
                        passport[selector] = part.rstrip()
                    i += 1
        passports.append(passport)

    # Counting the valid passports
    count = 0
    for passport in passports:
        if validate_passport(passport):
            count += 1

    print("Valid passports: {}".format(count))


if __name__ == "__main__":
    main()
