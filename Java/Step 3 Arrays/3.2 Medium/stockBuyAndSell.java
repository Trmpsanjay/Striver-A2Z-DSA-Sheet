class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int buyPrice = prices[0];
        // int sellPrice = prices[0];
        for (int price : prices) {
            if (price<buyPrice){
                buyPrice = price;
            }else{
                int profit = price-buyPrice;
                if (profit > maxProfit){
                    maxProfit = profit;
                }
            }
        }
        return maxProfit;
    }
}