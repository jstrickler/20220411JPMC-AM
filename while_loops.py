# while EXPR:
#     code
#     code
#     ...

i = 0
while i < 3:
    print(i, "Python")
    i += 1
print()

while True:
    user_name = input("User name: ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        print("Please enter a name")
        continue # go to top
    print(f"Adding {user_name}")

