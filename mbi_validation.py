"""
Validation per https://www.cms.gov/medicare/new-medicare-card/understanding-the-mbi.pdf
C - Numeric 1 through 9
N - Numeric 0 through 9
AN - Either A or N
A - Alphabetic Character (A...Z); Excluding (S, L, O, I, B, Z)

1 - numeric values 1 through 9

2 - alphabetic values A through Z (minus S, L, O, I, B, Z)
5 - alphabetic values A through Z (minus S, L, O, I, B, Z)
8 - alphabetic values A through Z (minus S, L, O, I, B, Z)
9 - alphabetic values A through Z (minus S, L, O, I, B, Z)

3 - alphanumeric values 0 through 9 and A through Z (minus S, L, O, I, B, Z)
6 - alphanumeric values 0 through 9 and A through Z (minus S, L, O, I, B, Z)

4 - numeric values 0 through 9
7 - numeric values 0 through 9
10 - numeric values 0 through 9
11 - numeric values 0 through 9
"""


def is_numeric(mbi: str, start_at_zero=True):
    if start_at_zero:
        return mbi.isdigit()
    return mbi.isdigit() and mbi != "0"


def is_alpha(mbi: str):
    return mbi.isalpha() and mbi.lower() not in ["s", "l", "o", "i", "b", "z"]


def is_alphanumeric(mbi: str):
    return is_numeric(mbi) or is_alpha(mbi)
