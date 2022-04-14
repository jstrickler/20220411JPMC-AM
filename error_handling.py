file_path = "DATA/wombats.txt"

try:
    with open(file_path) as file_in:
        pass
except FileNotFoundError as err:
    print(err)

names = ['John', 'Paul', 'George', 'Ringo']
try:
    print(names[8])
except IndexError as err:
    print(err)

nums = [0, 800, 80, 0, 1000, 32, 255, "abc", 400, 5, 5000]
for num in nums:
    try:
        result = 5000 / num
    except (ZeroDivisionError, TypeError) as err:
        print(err)
        # log the error
        # provide alternate value
        # pop up a warning window
        # exit the program gracefully
    except ValueError as err:
        print(err)
    else:  # there were no exceptions
        print(result)

print("ALL DONE")

