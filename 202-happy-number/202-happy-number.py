class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        found = [n]
        while n != 1:
            n = sum(list(map(lambda x: int(x) ** 2, str(n))))
            if n in found:
                return False
            found.append(n)
        return True
