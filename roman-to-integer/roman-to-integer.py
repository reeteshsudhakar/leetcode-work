class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500, "M":1000}
        
        sum = 0
        prev_value = 1001

        for char in s: 
            value = roman[char]
            if value <= prev_value:
                sum += value
                prev_value = value
            else: 
                sum += value - 2 * prev_value
        return sum