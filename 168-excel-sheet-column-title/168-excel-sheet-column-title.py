class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while columnNumber > 0: 
            columnNumber, idx = divmod(columnNumber - 1, 26)
            result = alphabet[idx] + result
                    
        return result
        
        