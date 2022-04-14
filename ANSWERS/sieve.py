#!/usr/bin/env python
import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

flags = [True] * limit

count = 0
for num in range(2, limit):
    if flags[num]:
        count += 1
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            flags[multiple_of_num] = False
print()
print(f"There are {count} primes less than or equal to {limit -1}")