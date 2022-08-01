class Solution {
    public String intToRoman(int num) {
        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] numerals ={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            while (num >= nums[i]) {
                result.append(numerals[i]);
                num -= nums[i];
            }
        }
        
        return result.toString();
    }
}