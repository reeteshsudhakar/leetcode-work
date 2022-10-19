from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for char in s: 
            s_dict[char] += 1
        
        for char in t:
            t_dict[char] += 1
        
        return s_dict == t_dict
        