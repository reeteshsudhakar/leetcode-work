class Solution {
    public String longestCommonPrefix(String[] strs) {
        int count, len, i, j;
        count = strs[0].length();
        len = count;
        
        for (i = 1; i < strs.length; i++) {
            len = (len < strs[i].length()) ? len : strs[i].length();
            
            for (j = 0; j < len; j++) {
                if (strs[0].charAt(j) != strs[i].charAt(j)) {
                    break;
                }
            }
            
            if (j < count) {
                count = j;
            }
        }
        
        return strs[0].substring(0, count);
    }
}