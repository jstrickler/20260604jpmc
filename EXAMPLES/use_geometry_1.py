import sys
import os
import geometry  # load geometry.py


# MODULE.NAME
circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# module search path
# 1. current folder
# 2. folders in PYTHONPATH
# 3. installation-folder/lib*
print('-' * 60)
for path in sys.path:
    print(path)
print('-' * 60)
