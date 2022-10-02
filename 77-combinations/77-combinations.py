class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        def backtrack(combination, num):
            if len(combination) == k:
                ret.append(combination.copy())
                
            else:
                for i in range(num, n + 1):
                    combination.append(i)
                    backtrack(combination, i + 1)
                    combination.pop()
        
        backtrack([], 1)
                
        return ret