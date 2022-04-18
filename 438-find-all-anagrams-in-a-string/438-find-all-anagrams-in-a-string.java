class Solution {
    public List<Integer> findAnagrams(String text, String pattern) {
        if (pattern.length() > text.length() || text.length() == 0 || pattern.length() == 0) {
            return new ArrayList<Integer>();
        }

        int[] patternMap = new int[26];
        int[] textMap = new int[26];

        int start = 0;

        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i < pattern.length(); i++) {
            patternMap[pattern.charAt(i) - 'a']++;
        }

        for (int i = 0; i < text.length(); i++) {
            textMap[text.charAt(i) - 'a']++;
            if (i >= pattern.length()) {
                textMap[text.charAt(start) - 'a']--;
                start++;
            }
            if (Arrays.equals(textMap, patternMap)) {
                result.add(start);
            }
        }
        return result;
    }
}