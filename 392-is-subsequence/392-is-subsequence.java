class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0) {
            return true;
        } else if (s.length() > t.length()) {
            return false;
        }
        
        int i = 0;
        int j = 0;
        
        while (i < t.length() && j < s.length()) {
            if (t.charAt(i) == s.charAt(j)) {
                j++;
            }
            
            i++;
        }
        
        return j == s.length();
    }
}