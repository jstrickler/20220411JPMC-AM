mary_in = open('DATA/mary.txt', 'r')
mary_in.close()

# with EXPR as var:
# with EXPR:
# abs:  c:/.../.../DATA/mary.txt
# abs: //my_stuff/.../.../DATA/mary.txt
# rel:  DATA/mary.txt
file_path = 'DATA/mary.txt'
with open(file_path) as mary_in:
    for raw_line in mary_in:    # mary_in.readline()
        print("RAW:", repr(raw_line))
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

with open(file_path) as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)

word_file_path = "DATA/words.txt"
target = 'x'
output_file_name = f"{target}_words.txt"
with open(word_file_path) as words_in:
    with open(output_file_name, "w") as words_out:
        for word in words_in:
            if word.startswith(target):
                words_out.write(word)

with open('DATA/mary.txt', 'r') as mary_in:
    with open('upper_mary.txt', 'w') as upper_out:
        with open('lower_mary.txt', 'w') as lower_out:
            for line in mary_in:
                upper_out.write(line.upper())
                lower_out.write(line.lower())

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.upper() + '\n')




