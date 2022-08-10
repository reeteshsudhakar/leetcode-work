class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        int smallestValue = Integer.MAX_VALUE;
        
        for (int price : prices) {
            if (price < smallestValue) {
                smallestValue = price;
            }
            
            result = Math.max(result, price - smallestValue);
        }
        
        return result;
    }
}