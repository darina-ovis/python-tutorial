from typing import List


# Leetcode #2011. Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
def final_value_after_operations(operations: List[str]) -> int:
    x = 0
    for op in operations:
        if op == "X++" or op == "++X":
            x = x + 1
        else:
            x = x - 1
    return x



