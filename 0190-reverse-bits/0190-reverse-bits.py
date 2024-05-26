class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        
        for i in range(32):
            val = (n >> i) & 1
            ret += (val << (31 - i))
        
        return ret