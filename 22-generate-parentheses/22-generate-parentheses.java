class Solution {
        
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        if (n == 1) {
            result.add("()");
            return result;
        } else {
            generateStrings("", 0, 0, n, result);
            return result;
        }
    }
    
    public void generateStrings(String parentheses, int i, int j, int length, List<String> result) {
        if (parentheses.length() == length * 2) {
            result.add(parentheses);
            return;
        }
        
        if (i < length) {
            generateStrings(parentheses + "(", i + 1, j, length, result);
        } 
        
        if (j < i) {
            generateStrings(parentheses + ")", i, j + 1, length, result);
        }
        
    }
}