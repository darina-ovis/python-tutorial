from typing import List
import re


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


def phone_number_verify(phones: List[str]) -> List[bool]:
    result: List[bool] = []
    for phone in phones:
        result.append(re.match("[7-8][0-9]{9}$", phone) is not None)
    return result
