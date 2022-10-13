from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        
        for string in strs:
            counter = [0] * 26
            for char in string: 
                counter[ord(char) - ord('a')] += 1
            ret[tuple(counter)].append(string)
            
        return ret.values()
            
                