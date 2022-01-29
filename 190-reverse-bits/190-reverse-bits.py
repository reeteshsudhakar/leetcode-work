class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bits = 32
        result = 0
        for i in range(bits):
            result = result << 1 
            result = result + (n & 1) 
            n = n >> 1 
        return result
