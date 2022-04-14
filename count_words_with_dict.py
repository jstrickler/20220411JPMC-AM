counts = {}

file_path = 'DATA/words.txt'

with open(file_path) as words_in:
    for word in words_in:
        first_letter = word[0]  # first character of str
        if first_letter in counts:
            counts[first_letter] += 1
            # counts[first_letter] = counts[first_letter] + 1
        else:
            counts[first_letter] = 1

for word, count in counts.items():
    print(f"{count:6d} {word}")

