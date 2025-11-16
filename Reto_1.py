def unlock_door(initial_code, commands):
    code = [int(digit) for digit in str(initial_code)]
    iterator = 0
    for command in commands:
        match command:
            case "L":
                iterator = (iterator - 1) % len(code)
            case "R":
                iterator = (iterator + 1) % len(code)
            case "D":
                code[iterator] -= 1
                if code[iterator] < 0:
                    code[iterator] = 9
            case "U":
                code[iterator] += 1
                if code[iterator] > 9:
                    code[iterator] = 0
    return ''.join(map(str, code))


print(unlock_door(528934712834, "URDURUDRUDLLLLUUDDUDUDUDLLRRRR"))
