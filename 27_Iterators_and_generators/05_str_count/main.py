import os


def py_string(directory):
    for elem in os.listdir(os.path.join(directory)):
        if elem.endswith('.py'):
            with open(os.path.join(directory, elem), 'r', encoding='utf-8') as file:
                for i_line in file:
                    if i_line.startswith('#') or len(i_line) < 1:
                        pass
                    else:
                        yield 1


lines = 0
for i in py_string('/Users/kron/python-ds/26_OOP_principles/07_stack'):
    lines += 1

print(lines)
