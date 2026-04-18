def get_number_constraint(n: int, c: int) -> str:
    number: str = str(n)

    max_number: list[int] = []

    constraint_fount: bool = False

    for digit_str in number:
        digit:int = int(digit_str)

        if c == 9:
            if constraint_fount:
                digit = 8

            else:
                if digit == c:
                    constraint_fount = True
                    digit -= 1

        elif digit == 0:
            # If constraint = 0 then go up and subtract 1 from previous digit
            digit = 9

            holder_digit: int = max_number.pop()
            holder_digit -= 1
            max_number.append(holder_digit)

        else:
            digit -= 1

        max_number.append(digit)

    return ''.join(map(str, max_number))

get_number:int = int(input("Please enter a number: "))
get_constraint: int = int(input("Please enter a constraint: "))

print(get_number_constraint(get_number, get_constraint))
