def check_steps():
    with open("trace.txt", "r") as steps_file:
        total_steps = 0
        last_steps = 0
        line = steps_file.read().strip().splitlines()
        for steps in line:
            last_steps = 0
            pos = 0
            steps = [int(s) for s in steps.split()]
            max_pos = len(steps)
            iterator = 0
            while pos >= 0 and pos < max_pos:
                pos += steps[iterator]
                steps[iterator] += 1
                iterator = pos
                total_steps += 1
                last_steps += 1

        print(f"submit {total_steps}-{last_steps}")


check_steps()
