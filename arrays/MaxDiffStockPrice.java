package arrays;

/*
121. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

*/

public class MaxDiffStockPrice {

    public static int maxProfit(int[] prices) {
        if (prices.length == 0 || prices.length == 1) {
            return 0;
        }

        int maxDiff = prices[1] - prices[0];
        int minElem = prices[0];
        int currentDiff;
        for (int i = 1; i < prices.length; i++) {
            currentDiff = prices[i] - minElem;
            if (currentDiff > maxDiff) {
                maxDiff = currentDiff;
            }
            if (prices[i] < minElem) {
                minElem = prices[i];
            }
        }
        if (maxDiff < 0) {
            return 0;
        }
        return maxDiff;
    }

    public static void main(String args[]) {
        int[] nums = new int[] { 7, 1, 5, 3, 6, 4 };
        System.out.println("result = " + maxProfit(nums));
    }
}
