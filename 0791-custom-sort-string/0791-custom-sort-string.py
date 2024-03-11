class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """

        counter = {item : 0 for item in order}

        for char in s:
            if char in counter: counter[char] += 1
        
        ret = ''

        for char in order:
            ret += counter[char] * char

        for char in s:
            if char not in order:
                ret += char

        return ret



