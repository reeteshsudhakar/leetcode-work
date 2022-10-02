class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        
        def backtrack(size, combination, num):
            if size == 0:
                ret.append(combination.copy())
            
            else: 
                for i in range(num, n + 1):
                    combination.append(i)
                    backtrack(size - 1, combination, i + 1)
                    combination.pop()
        
        backtrack(k, [], 1)
        
        return ret