class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recurse(curr_string: str, cache: Dict[str, bool] = {}) -> bool:
            # return cached result
            if curr_string in cache: return cache[curr_string]
            
            # base case - if we've reached an empty string we've segmented properly
            if not curr_string: return True
            
            for word in wordDict:
                # if the current string starts with a word, we can segment
                if curr_string.startswith(word):
                    
                    # recursing to see if later segments work
                    if recurse(curr_string[len(word):], cache):
                        
                        # if success, cache the result and return True
                        cache[curr_string] = True
                        return True
            
            # segmenting did not work, cache result and return False
            cache[curr_string] = False
            return False
        
        # recurse on the given string
        return recurse(s)