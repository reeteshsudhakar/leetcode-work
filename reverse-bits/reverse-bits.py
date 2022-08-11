class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bin_string = bin(n)[2:]
        
        while len(bin_string) < 32:
            bin_string = "0" + bin_string
        
        result = 0
        multiplier = 1
        idx = 0
        
        while idx < len(bin_string):
            if bin_string[idx] == "1":
                result += multiplier
            
            multiplier *= 2
            idx += 1
        
        return result
        