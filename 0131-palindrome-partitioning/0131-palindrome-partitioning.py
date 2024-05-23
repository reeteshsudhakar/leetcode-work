class Solution:
    def partition(self, s: str) -> List[List[str]]:
#         ret = []
        
#         def check_palindrome(arr: List[str]) -> bool:
#             for item in arr: 
#                 if item != item[::-1]: 
#                     return False
#             return True
        
#         def dfs(idx: int, curr_arr: List[str]):
#             if idx == len(s):
#                 if check_palindrome(curr_arr) and curr_arr not in ret: 
#                     ret.append(curr_arr)
#                 return
            
#             dfs(idx + 1, curr_arr + [s[idx]])
            
#             diff_arr = curr_arr.copy()
#             if len(diff_arr) > 0: 
#                 diff_arr[-1] += s[idx]
#             else: 
#                 diff_arr += s[idx]
            
#             dfs(idx + 1, diff_arr)
        
#         dfs(0, [])
#         return ret

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
        