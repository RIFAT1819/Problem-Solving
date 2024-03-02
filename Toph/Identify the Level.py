import math

def min_level_number(N):
    # Find the minimum level number of the node
    return math.ceil(math.log2(N + 1))

# Input number of test cases
T = int(input())

# Iterate through each test case
for case in range(1, T + 1):
    # Input number of nodes for each test case
    N = int(input())
    # Output the minimum level number for the given number of nodes
    print("Case {}: {}".format(case, min_level_number(N)))
