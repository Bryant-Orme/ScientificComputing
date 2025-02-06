def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        # Too many inputs
        return 'Error: Too many problems.'
    for prob in problems:
        # Operator not '+' or '-'
        print(prob.split()[1])
        if prob.split()[1] == '/' or prob.split()[1] == '*':
            return "Error: Operator must be '+' or '-'."
        nums = prob.split(' ')
        num1 = nums[0]
        num2 = nums[2]
        if not num1.isnumeric() or not num2.isnumeric():
            # Parameter contains non-numeric values
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            # Operands larger than 4 digits
            return 'Error: Numbers cannot be more than four digits.'

    top = ''
    bottom = ''
    line = ''
    answers = ''
    for prob in problems:
        num1 = prob.split()[0]
        operator = prob.split()[1]
        num2 = prob.split()[2]
        length = max(len(num1), len(num2)) + 2
        top += num1.rjust(length, ' ') + '    '
        bottom += operator + num2.rjust(length - 1, ' ') + '    '
        line += '-'.rjust(length, '-') + '    '
        if operator == '+':
            ans = int(num1) + int(num2)
        else:
            ans = int(num1) - int(num2)

        answers += str(ans).rjust(length, ' ') + '    '

    problems = top.rstrip() + '\n' + bottom.rstrip() + '\n' + line.rstrip()

    if show_answers:
        problems += '\n' + answers.rstrip()

    return problems
