class Password:

    def __init__(self, password):
        # Pull apart the text password
        password = password.split()

        numbers = password[0].split("-")
        self._lower = int(numbers[0])
        self._upper = int(numbers[1])

        self._letter = password[1][0]

        self._password = password[2]

    def is_legal(self):
        total = 0
        for char in self._password:
            if char == self._letter:
                total += 1

        return self._lower <= total <= self._upper

    def is_legal_the_second(self):
        return (self._password[self._lower - 1] == self._letter) != (self._password[self._upper - 1] == self._letter)


def main():
    # Create the password objects
    passwords = []
    with open("input.txt") as accounting:
        for line in accounting:
            passwords.append(Password(line))

    # Count valid passwords
    valid_passwords = 0
    for password in passwords:
        if password.is_legal_the_second():
            valid_passwords += 1

    print("Valid passwords: {}".format(valid_passwords))


if __name__ == "__main__":
    main()
