alphabet = 'abcdefghijklmnopqrstuvwxyz'

file = open('text.txt', 'r')
new_file = open('cipher_text.txt', 'w')
line_num = 1

for i_line in file:
    for char in i_line:
        if char == '\n':
            new_file.write('\n')
        else:
            letter = alphabet[(alphabet.index(char.lower()) + line_num) % len(alphabet)]
            new_file.write(letter)
    line_num += 1

file.close()
new_file.close()
