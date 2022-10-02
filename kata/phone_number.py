from typing import List
import re


def phone_number_verify(phones: List[str]) -> List[bool]:
    result: List[bool] = []
    for phone in phones:
        result.append(re.match("[7-8][0-9]{9}$", phone) is not None)
    return result
