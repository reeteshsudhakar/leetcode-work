class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        str_x = str(bin(x))[2:]
        str_y = str(bin(y))[2:]
        
        if (len(str_x) < len(str_y)):
            while (len(str_x) < len(str_y)):
                str_x = "0" + str_x
        elif (len(str_y) < len(str_x)):
            while (len(str_y) < len(str_x)):
                str_y = "0" + str_y
        
        print(str_x)
        print(str_y)
        
        result = 0
        
        for i in range(len(str_x)):
            if str_x[i] != str_y[i]:
                result += 1
        
        return result