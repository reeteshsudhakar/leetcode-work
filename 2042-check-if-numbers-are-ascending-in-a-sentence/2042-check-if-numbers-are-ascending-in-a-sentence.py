class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        numbers = filter(lambda char : char.isdigit(), s.split(" "))
        previous_number = float('-inf')
        
        for number in numbers:
            if int(number) > previous_number:
                previous_number = int(number)
            else:
                return False
        return True
        