class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0 
        while n != 0:
            if n & 1 == 1:
                ret += 1
            n >>= 1
        
        return ret