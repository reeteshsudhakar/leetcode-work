class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        result = ""
        for i in range(len(roman_numerals)):
            while True:
                if num // roman_numerals[i][0] != 0:
                    num = num - roman_numerals[i][0]
                    result += roman_numerals[i][1]
                else:
                    break
        
        return result
            
        