class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        inputNum = str(bin(n))
        for i in inputNum:
            if i == "1":
                count += 1
        return count