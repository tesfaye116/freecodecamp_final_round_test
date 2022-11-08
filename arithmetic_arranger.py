def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        first_line = ""
        second_line = ""
        third_line = ""
        result_line = ""
        for problem in problems:

            first_num, operator, second_num = problem.split()

            if not first_num.isdigit() or not second_num.isdigit():
                return "Error: Numbers must only contain digits."
            if len(first_num) > 4 or len(second_num) > 4:
                return "Error: Numbers cannot be more than four digits."
            if operator == "+":
                result = int(first_num) + int(second_num)
            elif operator == "-":
                result = int(first_num) - int(second_num)
            else:
                return "Error: Operator must be '+' or '-'."
            first_num = str(first_num)
            second_num = str(second_num)
            result = str(result)
            first_line += first_num.rjust(max(len(first_num),
                                          len(second_num)) + 2) + "   "
            second_line += operator + \
                second_num.rjust(
                    max(len(first_num), len(second_num)) + 1) + "   "
            third_line += "-" * \
                (max(len(first_num), len(second_num)) + 2) + "   "

            result_line += result.rjust(
                max(len(first_num), len(second_num)) + 2) + "   "

        arranged_problems = first_line + "\n" + second_line + \
            "\n" + third_line + "\n" + result_line
        return arranged_problems
