class Solution:
    def isPalindrome(self, s: str) -> bool:
        ret = ''
        
        for i in range(len(s)):
            if s[i].isalnum(): ret += s[i].lower()
        
        return ret == ret[::-1]