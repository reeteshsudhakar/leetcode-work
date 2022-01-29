class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        
        if n == 0:
            return result
        else: 
            for num in range(1, n + 1):
                binString = (str(bin(num))[2::])
                count = 0
                for i in binString:
                    if i == "1":
                        count += 1
                result.append(count)
        return result
            