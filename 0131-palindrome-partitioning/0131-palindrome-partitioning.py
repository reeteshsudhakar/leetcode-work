class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
        def check_palindrome(val: str) -> bool:
            return val == val[::-1]
        
        def dfs(idx: int, curr_arr: List[str]):
            if idx == len(s):
                ret.append(curr_arr[:])
                return
            
            for i in range(idx + 1, len(s) + 1):
                if check_palindrome(val=s[idx:i]):
                    dfs(i, curr_arr + [s[idx:i]])
        
        dfs(0, [])
        return ret
        