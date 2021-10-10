import unittest
lookUp2 = { 
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
    """
    analyse each of the 4 digits in turn
    """
    digits = list(str(decimal + 10000)) # make sure leading zeros are included
    # build list of digits (ignoring first digit)
    symbols = list()
    symbols.append(lookUp2[int(digits[1])*1000])
    symbols.append(lookUp2[int(digits[2])* 100])
    symbols.append(lookUp2[int(digits[3])*  10])
    symbols.append(lookUp2[int(digits[4])*   1])
    return "".join(symbols)

def romanToDecimal(roman):
    decimal = 0
    previous = 0
    for ch in roman[::-1]:
        if ch == 'M': this = 1000
        if ch == 'D': this = 500
        if ch == 'C': this = 100
        if ch == 'L': this = 50
        if ch == 'X': this = 10
        if ch == 'V': this = 5
        if ch == 'I': this = 1
        if this >= previous: 
            decimal = decimal + this
        else:
            decimal = decimal - this
        previous = this
    return decimal

# assert(expected, actual)
class MyTests(unittest.TestCase):
    def test_CanConvert5(self):
        self.assertEqual(5, romanToDecimal('V'))
     
    def test_CanConvertNumberBetween6and8(self):
        self.assertEqual(6, romanToDecimal('VI'))
        self.assertEqual(7, romanToDecimal('VII'))
        self.assertEqual(8, romanToDecimal('VIII'))
      
    def test_CanConvertNumberBetween1and3(self):
        self.assertEqual(1, romanToDecimal('I'))
        self.assertEqual(2, romanToDecimal('II'))
        self.assertEqual(3, romanToDecimal('III'))
  
    def test_CanConvert4(self):
        self.assertEqual(4, romanToDecimal('IV'))
  
    def test_CanConvertNumberBetween9and13(self):
        self.assertEqual(9, romanToDecimal('IX'))
        self.assertEqual(11, romanToDecimal('XI'))
        self.assertEqual(13, romanToDecimal('XIII'))
     
    def test_CanConvertNumberBetween14and39(self):
        self.assertEqual(14, romanToDecimal('XIV'))
        self.assertEqual(19, romanToDecimal('IXX'))
        self.assertEqual(23, romanToDecimal('XXIII'))
        self.assertEqual(34, romanToDecimal('XXXIV'))
        self.assertEqual(37, romanToDecimal('XXXVII'))
    
    def test_CanConvertNumberBetween40and70(self):
        self.assertEqual(44, romanToDecimal('XLIV'))
        self.assertEqual(69, romanToDecimal('LXIX'))
    
    def test_CanConvertNumberBetween71and250(self):
        self.assertEqual(87, romanToDecimal('LXXXVII'))
        self.assertEqual(239, romanToDecimal('CCXXXIX'))
    
    def test_CanConvertLargeNumber(self):
        for n in range(1, 4001):
            self.assertEqual(n, romanToDecimal(decimalToRoman(n)))
    
#     def setUp(self):
#         """
#         set up data used in the tests.
#         setUp is called before each test function execution.
#         """
#         self.point = pass

def suite():
    suite = unittest.TestSuite()
    suite.addTest(MyTests('test_CanConvertNumberBetween6and8'))
    return suite

if __name__ == '__main__':
#    unittest.TextTestRunner(verbosity=2).run(suite())
    unittest.main(verbosity=0)