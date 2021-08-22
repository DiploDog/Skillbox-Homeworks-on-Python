file = open('numbers.txt', 'r')
summa = 0
for i_line in file:
    for i_element in i_line:
        if i_element.isalnum():
            summa += int(i_element)
file.close()
new_file = open('answer.txt', 'w')
new_file.write(str(summa))
new_file.close()
