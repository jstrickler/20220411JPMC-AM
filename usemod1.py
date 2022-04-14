# from john/math run geometry.py
from john.math import geometry

a1 = geometry.circle_area(15)
print("a1: {}".format(a1))

a2 = geometry.rectangle_area(8, 19)
print("a2: {}".format(a2))

# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders

import sys
for path in sys.path:
    print(path)




