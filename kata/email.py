from typing import List
import re


def email_check (email) -> bool:
    return re.fullmatch("\w+@\w+[.]\w{2,}", email) is not None