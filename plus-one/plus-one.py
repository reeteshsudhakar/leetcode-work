class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = ''
        for i in digits: 
            num += str(i)
        output = int(num) + 1
        list_output = []
        for i in str(output):
            list_output.append(str(i))
        return list_output
        