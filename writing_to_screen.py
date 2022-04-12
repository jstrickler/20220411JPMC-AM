person = "George Washington"
city = "Philadelphia"
value = 1776.0704

print(person, city, value)
# output str(person) + sep + str(city) + sep + str(value) + end

print(person, city, value, sep='')
print(person, city, value, sep='/')
print(person)
print(city)
print(value)
print(person, end=" ")
print(city, end=":")
print(value)

print("value: {}".format(value))

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print(f"{person} lives in {city}")  # f-string


print("value: {:.1f}".format(value))
print(f"value is {value:.1f}")

big_number = 2_395_723_590_273_520_937
print(f"number is {big_number:,d}")


