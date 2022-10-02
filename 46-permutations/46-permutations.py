class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def backtrack(permutation, k):
            if len(k) == 0:
                ret.append(permutation.copy())
            else:
                for i in range(len(k)):
                    permutation.append(k[i])
                    new_k = k[:i] + k[i + 1:]
                    backtrack(permutation, new_k)
                    permutation.pop()
                    
        backtrack([], nums.copy())
        
        return ret
    
    