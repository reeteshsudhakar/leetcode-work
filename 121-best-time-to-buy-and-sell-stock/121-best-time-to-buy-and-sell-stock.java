class Solution {
    public int maxProfit(int[] prices) {
        int result = 0;
        int smallestValue = 10001;
        
        for (int price : prices) {
            if (price < smallestValue) {
                smallestValue = price;
            } else {
                result = Math.max(result, price - smallestValue);
            }
        }
        
        return result;
    }
}