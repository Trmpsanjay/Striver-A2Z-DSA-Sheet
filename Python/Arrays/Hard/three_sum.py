from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        LeetCode 15: 3Sum
        Return all UNIQUE triplets [a, b, c] such that a + b + c == 0.

        Alternate approach (as you noted from pepcoding):
        - using hashmap + sorting
        - ensure uniqueness by encoding triplet like:
          (((num1 * 10**5) + num2) * 10**5) + num3

        Optimal approach used here:
        ✅ Sort + fix one number + two pointers
        - Sorting helps:
          1) two-pointer movement
          2) easy duplicate skipping (uniqueness)

        Time: O(n^2)
        Space: O(1) extra (ignoring output)
        """

        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            # fixing nums[i]; skip duplicates for i to avoid repeating same triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # optional early stop: once nums[i] > 0, all next are >= 0, sum can't be 0
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])

                    # move both pointers inward (then skip duplicates)
                    j += 1
                    k -= 1

                    # slide j unless distinct number is found
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # slide k unless distinct number is found
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s > 0:
                    # sum too big -> decrease it by moving k left
                    k -= 1
                else:
                    # sum too small -> increase it by moving j right
                    j += 1

        return ans
