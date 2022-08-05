class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> stringMap = new HashMap<>();
        int counter = 0;
        int i = 0;
        int j = 0;
        
        while (i < s.length()) {
            if (!stringMap.containsKey(s.charAt(i))) {
                stringMap.put(s.charAt(i), 1);
                i++;
                counter = Math.max(counter, stringMap.size());
            } else {
                stringMap.remove(s.charAt(j));
                j++;
            }
        }
        
        return counter;
    }
}