class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character> sStack = new Stack<>();
        Stack<Character> tStack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '#') {
                if (sStack.isEmpty()) {
                    continue;
                } else {
                    sStack.pop();
                }
            } else {
                sStack.push(s.charAt(i));
            }
        }
        
        for (int j = 0; j < t.length(); j++) {
            if (t.charAt(j) == '#') {
                if (tStack.isEmpty()) {
                    continue;
                } else {
                    tStack.pop();
                }
            } else {
                tStack.push(t.charAt(j));
            }
        }

        return sStack.equals(tStack);
    }
}