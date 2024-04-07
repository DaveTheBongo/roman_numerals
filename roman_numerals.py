""" roman_numerals.py
    int_to_roman() Converts int to roman numerals
    roman_to_int() Converts roman numerals to int
    (Accurate to 3,999,999 if 3 consecutive chr max)
"""

roman = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1_000,
    "MV\u0304": 4_000,
    "V\u0304": 5_000,
    "MX\u0304": 9_000,
    "X\u0304": 10_000,
    "X\u0304L\u0304": 40_000,
    "L\u0304": 50_000,
    "X\u0304C\u0304": 90_000,
    "C\u0304": 100_000,
    "C\u0304D\u0304": 400_000,
    "D\u0304": 500_000,
    "C\u0304M": 900_000,
    "M\u0304": 1_000_000,
}


def roman_to_int(s: str) -> int:
    """Convert Roman numerals to int"""

    def split_numerals(s: str) -> list:
        """Split str into Roman numerals"""
        l, i, numerals = len(s), 0, []
        while i < l:
            if i + 1 < l and s[i + 1] == "\u0304":
                numerals.append(s[i].upper() + s[i + 1])
                i += 2
            else:
                numerals.append(s[i].upper())
                i += 1
        return numerals

    numerals = split_numerals(s)
    l, total, i = len(numerals), 0, 0
    while i < l:
        if i + 1 < l:
            double = numerals[i] + numerals[i + 1]
            if double in roman:
                total += roman[double]
                i += 2
                continue
        total += roman[numerals[i]]
        i += 1
    return total


def int_to_roman(n: int) -> str:
    """Convert int to Roman numerals"""
    numerals = ""
    for k, v in reversed(roman.items()):
        while n >= v:
            numerals += k
            n -= v
    return numerals


num = 1949
r = int_to_roman(num)
i = roman_to_int(r)
print(f"\n{i:,} is {r}\n")
