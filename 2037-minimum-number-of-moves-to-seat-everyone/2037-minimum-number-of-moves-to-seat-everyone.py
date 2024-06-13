class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        
        ret = 0
        for i in range(len(seats)):
            ret += abs(seats[i] - students[i])
        return ret
        