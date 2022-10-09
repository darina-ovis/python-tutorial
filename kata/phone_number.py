from typing import List
import re


def phone_number_verify(phones: List[str]) -> List[bool]:
    result: List[bool] = []
    for phone in phones:
        result.append(re.match("[7-8][0-9]{9}$", phone) is not None)
    return result


def password_verity(password: str) -> bool:
    return has_capital_letter(password) and hasDigit(password)


def has_capital_letter(password):
    return hasPattern('[A-Z]*', password)


def hasDigit(password):
    return hasPattern('\\d', password)

def hasPattern(pattern, password):
    return re.search(pattern, password) is not None
