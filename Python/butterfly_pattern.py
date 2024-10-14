"""
This program takes an integer 'n' as input and prints a butterfly pattern
with height and width 2n-1. The pattern consists of stars ('*') and spaces,
forming two wings of the butterfly.

Input:
- An integer 'n' where n > 0.

Output:
- A butterfly pattern with 2n-1 rows and 2n-1 columns.
"""

n = int(input("Enter an integer n: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end='')
    for j in range(1, 2*(n-i)+1):
        print(' ', end='')
    for j in range(1, i+1):
        print('*', end='')
    print()

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print('*', end='')
    for j in range(1, 2*(n-i)+1):
        print(' ', end='')
    for j in range(1, i+1):
        print('*', end='')
    print()
