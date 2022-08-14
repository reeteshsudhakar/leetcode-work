class Solution {
    public int longestPalindrome(String s) {
        if (s.length() == 1) {
            return 1;
        }
        
        int[] counts = new int[256];
        
        for (int i = 0; i < s.length(); i++) {
            if (counts[s.charAt(i)] == 1) {
                counts[s.charAt(i)] = 0;
            } else {
                counts[s.charAt(i)] = 1;
            }
        }
        
        int result = 0;
        for (int i : counts) {
            result += i;
        }
        
        return result == 0 ? s.length() : s.length() - result + 1;
        
        
    }
}