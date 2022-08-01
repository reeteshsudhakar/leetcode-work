class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # initializing variables
        idx = 0
        length = len(s)
        sign = 1
        result = 0
        
        # clearing the white space
        while idx < length and s[idx] == " ":
            idx += 1
        
        # finding the sign of the digit
        if idx < length and s[idx] == "-":
            sign = -1
            idx += 1
        # passing the plus sign if found, not needed 
        elif idx < length and s[idx] == "+":
            idx += 1
        
        # parsing the digits and tallying the sum 
        while idx < length and s[idx].isdigit():
            result = result * 10 + int(s[idx])
            idx += 1
        
        # accounting for the sign in the string
        result *= sign 
        
        # returning the result based on constraints
        if (result > 2**31 - 1):
            return 2**31 - 1
        elif (result < -2**31):
            return -2**31
        else:
            return result