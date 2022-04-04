"""
Program to test and view de results of logic operations
"""

A = (True, True, False, False)
B = (True, False, True, False)

for i in A:
    for j in B:
        andOps = i and j
        print(f'{i} AND {j} = {andOps}')
        orOps = i or j
        print(f'{i} OR {j} = {orOps}')
