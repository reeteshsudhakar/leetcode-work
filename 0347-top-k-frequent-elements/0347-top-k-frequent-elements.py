from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = defaultdict(int)
        
        for num in nums:
            ret[num] += 1
        
        ret_list = sorted(ret.items(), key=lambda x: x[1], reverse=True)
        
        return [item[0] for item in ret_list][:k]