# -*- coding: utf-8 -*-
"""v3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TXC2mciyYtl34qI7tCfvusZ82a5ssjGA
"""

# document weather prediction project using github.
# Open the file to read values
with open("input.txt", "r") as file:
    # Read each line and split on '=' to extract the value
    a = int(file.readline().strip().split('=')[1])
    b = int(file.readline().strip().split('=')[1])
    c = int(file.readline().strip().split('=')[1])
    x = float(file.readline().strip().split('=')[1])

# Calculate y
y = (a * (x ** 2)) + (b * x) + c

# Output the value of y
print("Value of y:", y)
