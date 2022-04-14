x = 100  # global (to the file)

def spam():
    y = 99  # local
    print("In spam(): x is", x)
    print("In spam(): y is", y)

spam()
# print("in main: y is", y)
