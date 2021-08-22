from zipfile import ZipFile
ZipFile('voyna-i-mir.zip').extractall()

chars_dict = dict()

file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
for i_line in file:
    for char in i_line:
        if char.isalpha():
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

sorted_chars = dict()
sorted_by_val = sorted(chars_dict, key=chars_dict.get)

for letter in sorted_by_val:
    sorted_chars[letter] = chars_dict[letter]

for key, value in sorted_chars.items():
    print('{}: {}'.format(key, value))
