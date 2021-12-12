class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == "":
            return 0
        elif haystack == "" and len(needle) != 0:
            return -1
        
        
        length = len(needle)
        idx_range = [0, length]
        
        while idx_range[1] <= len(haystack):
            if haystack[idx_range[0]:idx_range[1]] == needle:
                return idx_range[0]
            
            idx_range[0] += 1
            idx_range[1] += 1
        
        return -1