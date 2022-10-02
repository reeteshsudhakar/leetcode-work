class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        if turnedOn > 8:
            return ret
        
        bits = "0000000000"
        
        def backtrack(left_to_enable, bits, k):
            if left_to_enable == 0:
                minutes = int(bits[4:], 2)
                hours = int(bits[:4], 2)
                
                if minutes < 10 and hours < 12:
                    ret.append(str(hours) + ":0" + str(minutes))
                elif minutes < 60 and hours < 12:
                    ret.append(str(hours) + ":" + str(minutes))
            else:
                for i in range(k, 10):
                    if bits[i] == "0":
                        bits = bits[:i] + "1" + bits[i + 1:]
                        backtrack(left_to_enable - 1, bits, i)
                        bits = bits[:i] + "0" + bits[i + 1:]
        
        backtrack(turnedOn, bits, 0)
        
        return ret