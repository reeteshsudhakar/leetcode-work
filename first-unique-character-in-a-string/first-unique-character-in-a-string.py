class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        for i in range(len(s)):
            if i == len(s) - 1:
                if s[i] not in s[:i]:
                    return i
            else: 
                if s[i] not in s[:i] and s[i] not in s[i + 1:]:
                    return i
        
        return -1