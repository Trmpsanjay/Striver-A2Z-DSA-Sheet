from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Maximum Product Subarray (LeetCode 152)

        Core observations (why prefix + suffix works):

        1) All positives (e.g., [2,3,4]):
           - Best subarray is usually the whole array / whole segment.
           - Prefix keeps growing, suffix also keeps growing.
           - max_ans becomes product of full segment.

        2) Even number of negatives in a segment (e.g., [-1,-2,3,4] OR [-1,-2]):
           - Product of the whole segment becomes positive (neg * neg = pos).
           - Best is often the whole segment.
           - Prefix or suffix will capture it.

        3) Odd number of negatives in a segment (e.g., [2,3,-2,4] or [-1,2,3]):
           - Product of whole segment is negative.
           - To get maximum positive product, you must DROP exactly one negative:
             either:
               - drop everything up to and including the first negative
               OR
               - drop everything after and including the last negative
           - Prefix scan captures "drop suffix after last negative" cases.
           - Suffix scan captures "drop prefix before first negative" cases.
           => Taking max of both directions covers both options.

        4) Zeros split the array into independent segments (e.g., [1,-2,0,3,-4]):
           - Any subarray crossing a zero has product 0.
           - So we treat each part between zeros separately.
           - Resetting product to 1 after we hit 0 starts a fresh segment.
           - We reset AFTER updating max_ans so that 0 itself can be the answer.

        Algorithm idea:
        - Maintain running product from left (prefix_product)
        - Maintain running product from right (suffix_product)
        - Update max_ans with max(prefix_product, suffix_product) each step
        - Reset products to 1 when they become 0 (new segment)

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """

        prefix_product = 1
        suffix_product = 1
        max_ans = float('-inf')
        n = len(nums)

        for i in range(n):
            # Running product from the left
            prefix_product *= nums[i]

            # Running product from the right
            suffix_product *= nums[n - 1 - i]

            # Best answer so far could appear in either direction
            max_ans = max(max_ans, prefix_product, suffix_product)

            # Zero breaks segments; reset AFTER considering current products
            if prefix_product == 0:
                prefix_product = 1
            if suffix_product == 0:
                suffix_product = 1

        return max_ans
