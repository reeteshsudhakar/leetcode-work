class Solution {
    public boolean isValid(String s) {
        Stack <Character> answer = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '{' || s.charAt(i) == '[' || s.charAt(i) == '(') {
                answer.push(s.charAt(i));
            } else if (!answer.isEmpty() && s.charAt(i) == '}' && answer.peek() == '{') {
                answer.pop();
            } else if (!answer.isEmpty() && s.charAt(i) == ']' && answer.peek() == '[') {
                answer.pop();
            } else if (!answer.isEmpty() && s.charAt(i) == ')' && answer.peek() == '(') {
                answer.pop();
            } else {
                answer.push(s.charAt(i));
            }
        }
        
        if (answer.isEmpty()) {
            return true;
        }
        
        return false; 
    }
}