
input_text = '''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''


lines = input_text.split('\n')


num_lines = len(lines)
words_in_each_line = [len(line.split()) for line in lines]

print(f'Number of lines: {num_lines}')
print('Number of words in each line:')
for i in range(num_lines):
    print(f'Line {i + 1} {words_in_each_line[i]}')
