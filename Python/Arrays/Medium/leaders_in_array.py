from typing import List

class Solution:
    def leaders(self, arr: List[int]) -> List[int]:
        """
        url : https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
        Find all "leaders" in the array.

        Definition:
        - arr[i] is a leader if it is >= every element to its right.
        - The rightmost element is always a leader (nothing on its right).

        Intuition (layman):
        - Scan from RIGHT to LEFT while keeping the maximum value seen so far.
        - If the current element is >= that max, then nothing to its right is bigger,
          so it must be a leader.

        Real-life analogy:
        - Imagine you're standing at the RIGHT end of a street and looking LEFT at buildings.
          A building is "visible" if it is taller than or equal to every building closer to you
          (i.e., to its right). As you look left, you keep track of the tallest building seen so far.
          Whenever you find a building that matches/exceeds this height, it becomes visible (a leader).

        Complexity:
        - Time: O(n) (single backward scan)
        - Space: O(k) for the output list (k = number of leaders)

        Common pain points / mistakes:
        1) Checking every element to the right for every index -> becomes O(n^2).
        2) Forgetting to reverse:
           - We collect leaders from right-to-left, but output must be left-to-right.
        3) Using '>' instead of '>=':
           - If duplicates exist, ">=” matters (both can be leaders).
        4) Initializing max as 0:
           - Breaks for all-negative arrays; safest is start with last element.
        """
        # Start from the last element (always a leader)
        curr_max = arr[len(arr) - 1]
        ans = [arr[len(arr) - 1]]

        # Traverse from right to left
        for i in range(len(arr) - 2, -1, -1):
            # If current element is >= the max seen so far from the right,
            # it means it is not smaller than anything on its right -> leader
            if arr[i] >= curr_max:
                ans.append(arr[i])      # add leader (note: this is reverse order)
                curr_max = arr[i]       # update max from the right

        # Reverse because we collected leaders from right -> left
        ans.reverse()
        return ans
