file = open('text.txt', 'r')
char_count = 0
chars_dict = dict()
for i_line in file:
    for char in i_line:
        if char.isalpha():
            char_count += 1
            char = char.lower()
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

for key, value in chars_dict.items():
    chars_dict[key] = round(value / char_count, 3)

values_dict = {value: [i for i in chars_dict.keys()
                       if chars_dict.get(i) == value]
               for value in chars_dict.values()}

analysis = open('analysis.txt', 'w')

for freq, char_list in values_dict.items():
    for i_char in sorted(char_list):
        analysis.write('{}: {}\n'.format(i_char, freq))

file.close()
analysis.close()
