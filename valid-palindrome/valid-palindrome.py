class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output = ""
        for char in s:
            if char.isalnum():
                output += char.lower()
        return output == output[::-1]