class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = "".join([char.lower() for char in s if char.isalnum()])
        print(string)
        
        return string == string[::-1]