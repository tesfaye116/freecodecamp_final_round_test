def arithmetic_arranger(problems, results=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top = []
    bottom = []
    dashes = []
    spaces = '    '
    answers = []

# ["32 + 698", "3801 - 2", "50 + 50", "123 - 49", "12 + 3600"]

    for problem in problems:
        first = '  ' + problem.split()[0]
        second = problem.split(' ', 1)[1]
        difference_first = len(first) - len(second)
        difference_second = len(second) - len(first)

        width_first = len(problem.split()[0])
        width_second = len(problem.split()[2])

        if width_first > 4 or width_second > 4:
            return "Error: Numbers cannot be more than four digits."

        if second[0] != '+' and second[0] != '-':
            return "Error: Operator must be '+' or '-'."

        if first.lstrip().isdigit() != True or second[2:].isdigit() != True:
            return 'Error: Numbers must only contain digits.'

        if difference_first > 0:
            second = second[0] + ' ' * (difference_first + 1) + second[2:]
        elif difference_second > 0:
            first = ' ' * difference_second + first

        # Optional condition to display answers under problems:
        if results:
            if second[0] == '+':
                answer = int(first) + int(second[2:])
            else:
                answer = int(first) - int(second[2:])

            answer_to_string = str(answer)
            length_result = len(answer_to_string)
            answer_to_string = '  ' + answer_to_string
            length_maximum = max(
                [len(first.lstrip()), len(second[1:].lstrip())])

            if length_maximum > length_result:
                answer_to_string = ' ' * \
                    (length_maximum - length_result) + answer_to_string
            elif length_maximum < length_result:
                answer_to_string = answer_to_string[1:]

            answers.append(answer_to_string)

    # Append variables to lists
        top.append(first)
        bottom.append(second)
        dashes.append('-' * len(second))

    # Set spacing
        spaced_top = spaces.join(top)
        spaced_bottom = spaces.join(bottom)
        spaced_dashes = spaces.join(dashes)
        spaced_answers = spaces.join(answers)

    if results:
        arranged_problems = spaced_top + '\n' + spaced_bottom + \
            '\n' + spaced_dashes + '\n' + spaced_answers
    else:
        arranged_problems = spaced_top + '\n' + spaced_bottom + '\n' + spaced_dashes

    return arranged_problems
