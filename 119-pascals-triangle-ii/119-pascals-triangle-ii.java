class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<List<Integer>> triangle = generate(rowIndex + 1);
        return triangle.get(rowIndex);
    }
    
    public List<List<Integer>> generate(int numRows) {
        // result stored here 
        List<List<Integer>> result = new ArrayList<>();
        
        // outer loop to generate the specified number of rows
        for (int i = 0; i < numRows; i++) {
            
            // inner loop to create each level
            List<Integer> init = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                
                // outer 1's 
                if (j == 0 || j == i) {
                    init.add(1);
                } else {
                    // inner number calculations 
                    init.add(result.get(i - 1).get(j - 1) + result.get(i - 1).get(j)); 
                }
            }
            
            // adds each level to the list 
            result.add(init);
        }
        
        // returns expected output
        return result;
    }
}