class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dict to track the last seen index of each character
        d = {}
        
        # left pointer for window
        l = 0
        
        # return value
        ret = 0
        
        # creating the right index for the window 
        for r in range(len(s)):
            # if the character is unique, then we want to check whether the current window is larger than the max 
            if s[r] not in d: 
                ret = max(ret, r - l + 1)
            # in the case the character isn't unique 
            else: 
                # if the last seen index of this character is outside of the window, then we can still check if the current window is larger than the max
                if d[s[r]] < l: 
                    ret = max(ret, r - l + 1)
                # the last seen index of this character is in the window, so we've hit a duplicate and need to move the left pointer of the window 
                else: 
                    l = d[s[r]] + 1
            
            # updating the seen dictionary
            d[s[r]] = r
        
        # returning the longest substring
        return ret
            