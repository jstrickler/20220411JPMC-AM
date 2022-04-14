
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

person = ('Bill', 'Gates', 'Microsoft', '1955-10-24')

print("person: {}".format(person))
print("type(person): {}".format(type(person)))
print("person[0]: {}".format(person[0]))
print("person[1]: {}".format(person[1]))

# var1, var2, ... = iterable

# person[0], person[1], person[2], ...
first_name, last_name, product, dob = person
print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
print("people[0]: {}".format(people[0]))
print("people[0][0]: {}".format(people[0][0]))
print("people[0][0][0]: {}".format(people[0][0][0]))

for person in people:
    print(person)
print('-' * 60)

for person in people:
    print(person[0], person[1])
print('-' * 60)

for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = (next value of) people
    print(first_name, last_name)
print('-' * 60)

