print("\U0001F92F")

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
print(len(s1), len(s2), len(s3), len(s4), len(s5))
print(s1 == s2 == s3 == s4)
print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("Guido is the ex-\"BDFL\" of Python")  # horrible!
print("""Guido's the ex-"BDFL" of Python""")

a_query = """
select *
from customers
where account_number = '123456'
"""

print(s5)  # raw!

#  raw bytes
# print(list(s4.encode()))







