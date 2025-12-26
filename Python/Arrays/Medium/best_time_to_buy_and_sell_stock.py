from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Best Time to Buy and Sell Stock (single transaction)

        Goal:
        - Choose ONE day to buy and a later day to sell to maximize profit.
        - If no profit is possible, return 0.

        Core idea (intuition):
        - While scanning prices left → right, always remember the cheapest price so far (best day to buy).
        - For each current price, treat it as a possible selling price and compute:
              profit_if_sell_today = current_price - min_price_so_far
        - Keep the maximum profit seen.

        Layman / real-life example:
        Imagine you're tracking gold prices daily.
        - You want to buy at the lowest price you've seen so far.
        - Every day you ask: "If I sold today, how much would I make compared to my cheapest buy day?"
        - Update your best profit.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Common pain points / mistakes:
        1) Selling before buying:
           - You must ensure the buy day is before the sell day.
           - Tracking "min price so far" guarantees that.

        2) Resetting profit when price drops:
           - Profit should never be reset to 0 inside the loop.
           - Just keep max profit so far.

        3) Wrong condition like `elif num >= buy_price`:
           - It's not wrong, but it's redundant.
           - You can compute profit even if it's negative and then max with current profit.

        4) Tracking sell_price separately:
           - Not needed; the current price is your candidate sell price.

        5) Edge cases:
           - prices length is usually >= 1 in LeetCode, but in general code you might guard empty input.
        """
        buy_price = prices[0]  # minimum price seen so far (best buying price up to current day)
        max_profit = 0         # best profit found so far (0 if no profitable trade)

        # Start from day 1 because day 0 is our initial buy candidate
        for price in prices[1:]:
            if price < buy_price:
                # Found a cheaper day to buy -> update buy_price
                buy_price = price
            else:
                # Treat today as selling day; compute profit using the best buy_price so far
                max_profit = max(max_profit, price - buy_price)

        return max_profit
