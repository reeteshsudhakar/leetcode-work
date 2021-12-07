class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if (x >= -2**31) and (x <= 2**31 - 1):
            if str(x) == str(x)[::-1]:
                return True
        return False