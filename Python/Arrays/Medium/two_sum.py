class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition (hash map / dictionary):
        We want two numbers that add up to target.
        For each number x, the only number that can pair with it is:
            needed = target - x

        Layman example:
        Target = 10.
        If you currently have 7 in your hand, you immediately know you need 3.
        So you check: "Have I seen a 3 before?"
          - If yes -> you found the pair.
          - If no  -> remember 7 for later.

        Real-life example:
        Shopping budget:
        You have to buy exactly 2 items whose prices sum to a fixed budget (target).
        While scanning prices one by one:
          - For each price, you compute the remaining budget needed.
          - You keep a notebook (hash map) of prices you've already seen and their index.
          - The moment you see a price that completes a previous one, you stop.

        Why the map helps:
        - Looking up "have I seen needed before?" is O(1) average.
        - So whole solution becomes O(n) instead of O(n^2).

        map stores: value -> index (number -> where we saw it)
        """

        seen = {}  # dictionary to store {number: index}

        for i in range(len(nums)):
            needed = target - nums[i]  # what number would complete the pair?

            # If we've seen 'needed' before, we found the answer
            if needed in seen:
                return [seen[needed], i]

            # Otherwise, remember current number and its index for future pairing
            seen[nums[i]] = i

        # If no pair found (LeetCode usually guarantees one exists)
        return None
