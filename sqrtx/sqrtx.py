class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        low_bound = 0
        upper_bound = (x//2)+1
        middle = low_bound + ((upper_bound - low_bound) // 2)
        while low_bound <= upper_bound:
            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x:
                upper_bound = middle - 1
            else:
                low_bound = middle + 1
            
            middle = low_bound + ((upper_bound - low_bound) // 2)
        
        return upper_bound
