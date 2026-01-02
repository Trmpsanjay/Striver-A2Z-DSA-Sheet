from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Majority Element II (elements appearing more than n/3 times)

        Key fact:
        - There can be AT MOST 2 numbers that appear more than n/3 times.
          (Because 3 such numbers would require > n elements total.)

        Intuition (Boyer-Moore Voting, extended):
        - We try to "cancel out" different numbers.
        - Think of it like voting with 2 seats:
          * If a number matches candidate1 -> vote for candidate1
          * If it matches candidate2 -> vote for candidate2
          * If a candidate has 0 votes -> replace it with the new number
          * If it's a new number and both candidates have votes -> cancel both votes (count1--, count2--)
        - After this cancellation process, the ONLY possible winners left are the two candidates.
        - But candidates are not guaranteed to be valid, so we do a final counting pass.

        Real-life analogy:
        - You have 2 "buckets" for frequent numbers.
        - When a new different number comes and both buckets are occupied,
          you remove one item from each bucket (pair-cancel).
        - True frequent numbers survive these cancellations.

        Complexity:
        - Time: O(n) (two passes)
        - Space: O(1)

        Common pain points:
        1) Forgetting the 2nd pass verification:
           - Voting phase gives candidates, not final answer.
        2) Wrong threshold check:
           - Condition is "more than n/3" => count > n//3
           - Your threshold = n//3 + 1 and you use >=, which is equivalent.
        3) Candidate assignment conditions:
           - Use "count == 0 and num != other_candidate" to avoid both candidates becoming same.
        """

        # Two candidates (placeholders initially)
        num1 = float('-inf')
        num2 = float('inf')

        # counts for the two candidates
        count1 = 0
        count2 = 0

        # -------- 1) Voting / candidate selection pass --------
        for num in nums:
            if num == num1:
                # vote for candidate1
                count1 += 1
            elif num == num2:
                # vote for candidate2
                count2 += 1
            elif count1 == 0 and num != num2:
                # candidate1 slot empty -> take this number
                num1 = num
                count1 = 1
            elif count2 == 0 and num != num1:
                # candidate2 slot empty -> take this number
                num2 = num
                count2 = 1
            else:
                # num is different from both candidates and both have votes
                # cancel one vote from each (pair elimination)
                count1 -= 1
                count2 -= 1

        # -------- 2) Verification pass (must do!) --------
        # Reset counts and count actual occurrences of candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1

        # "more than n/3" means count >= (n//3 + 1)
        threshold = (len(nums) // 3) + 1

        result = []
        if count1 >= threshold:
            result.append(num1)
        if count2 >= threshold:
            result.append(num2)

        return result
