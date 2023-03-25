def arithmetic_arranger(problems, display=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'

  split_problems = [items.split(' ') for items in problems]
  answers, top_line, bottom_line, dashes, answers_line = list(), str(), str(
  ), str(), str()

  for index, items in enumerate(split_problems):
    if items[1] != '+' and items[1] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(items[0]) > 4 or len(items[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    try:
      num1 = int(items[0])
      num2 = int(items[2])
    except ValueError:
      return "Error: Numbers must only contain digits."
    answers.append(num1 + num2 if items[1] == '+' else num1 - num2)
    spaces = abs(len(items[0]) - len(items[2]))

    if len(items[0]) > len(items[2]):
      top_line += '  ' + items[0] + '    '
      bottom_line += items[1] + ' ' + ' ' * spaces + items[2] + '    '
      dashes += '-' * (len(items[0]) + 2) + '    '
      answers_line += ' ' * (
        (len(items[0]) + 2) - len(str(answers[index]))) + str(
          answers[index]) + '    '
    else:
      top_line += '  ' + ' ' * spaces + items[0] + '    '
      bottom_line += items[1] + ' ' + items[2] + '    '
      dashes += '-' * (len(items[2]) + 2) + '    '
      answers_line += ' ' * (
        (len(items[2]) + 2) - len(str(answers[index]))) + str(
          answers[index]) + '    '

  if display:
    return top_line.rstrip() + '\n' + bottom_line.rstrip(
    ) + '\n' + dashes.rstrip() + '\n' + answers_line.rstrip()
  else:
    return top_line.rstrip() + '\n' + bottom_line.rstrip(
    ) + '\n' + dashes.rstrip()
