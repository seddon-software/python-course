"""
Create two subroutines that convert a decimal number in the 
range 1 to 3999 to Roman numerals, and back.
"""

lookUp = { 
             0: '', 
             1: 'I', 
             2: 'II', 
             3: 'III', 
             4: 'IV', 
             5: 'V',
             6: 'VI', 
             7: 'VII', 
             8: 'VIII', 
             9: 'IX', 
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
           100: 'C',
           200: 'CC',
           300: 'CCC',
           400: 'CD',
           500: 'D',
           600: 'DC',
           700: 'DCC',
           800: 'DCCC',
           900: 'CM',
          1000: 'M',
          2000: 'MM',
          3000: 'MMM',
          4000: 'MMMM'
         }


def decimalToRoman(decimal):
    symbols = []
    digits = list(str(decimal + 10000)) # make sure leading zeros are included
    symbols.append(lookUp[int(digits[1])*1000])
    symbols.append(lookUp[int(digits[2])* 100])
    symbols.append(lookUp[int(digits[3])*  10])
    symbols.append(lookUp[int(digits[4])*   1])
    return "".join(symbols)

def romanToDecimal(roman):
    '''
    if a roman symbol is less than its successor it is negative
    '''
    decimal = 0
    previous = 0
    symbols = { 'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1 }
    for ch in roman[::-1]:  # work backwards
        this = symbols[ch]
        if this >= previous: 
            decimal = decimal + this
        else:
            decimal = decimal - this
        previous = this
    return decimal
    

for n in range(1, 4000):
    print(n, decimalToRoman(n))

for n in range(1, 4000):
    r = decimalToRoman(n)
    print(romanToDecimal(r))
