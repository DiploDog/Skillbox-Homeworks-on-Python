file = open('zen.txt', 'r')
for i_line in reversed(list(file)):
    print(i_line, end='')
