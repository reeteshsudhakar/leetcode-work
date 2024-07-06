class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        
        rounds_completed = time // (n - 1)
        time_left = time % (n - 1)
        
        return time_left + 1 if rounds_completed % 2 == 0 else n - time_left