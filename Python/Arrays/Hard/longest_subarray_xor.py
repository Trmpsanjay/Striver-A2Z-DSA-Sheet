from typing import List

class Solution:
    def subarraysWithXorK(self, nums: List[int], k: int) -> int:
        """
        Count subarrays whose XOR equals k.

        Core idea (Prefix XOR + frequency map):
        - Let pre_xor be XOR of nums[0..i]
        - XOR of subarray (j+1..i) = pre_xor[i] ^ pre_xor[j]
        - We want: pre_xor[i] ^ pre_xor[j] = k
          => pre_xor[j] = pre_xor[i] ^ k

        So for each element:
        1) update prefix XOR
        2) compute target = pre_xor ^ k
        3) add how many times target appeared before (those are valid subarrays ending here)
        4) store/update frequency of current pre_xor

        Why freq_map starts with {0:1}:
        - Handles subarrays that start from index 0.
        - If pre_xor == k at some point, then target = pre_xor ^ k = 0,
          and we should count that once.

        Layman analogy:
        - Think of pre_xor as a "running XOR fingerprint".
        - To get XOR=k ending at current index, you need to have seen a previous
          fingerprint equal to (current_fingerprint ^ k).

        Complexity:
        - Time: O(n)
        - Space: O(n)

        Common pain points:
        - Forgetting {0:1} misses subarrays starting at index 0.
        - Using sum logic for XOR (XOR uses ^, not -).
        - Using a set instead of frequency map (duplicates matter).
        """

        freq_map = {0: 1}  # prefix_xor 0 seen once (empty prefix)
        pre_xor = 0
        count = 0

        for num in nums:
            pre_xor ^= num                 # update running XOR
            target = pre_xor ^ k           # needed previous prefix XOR

            if target in freq_map:
                count += freq_map[target]  # add all ways to form XOR=k ending here

            # record current prefix XOR frequency
            freq_map[pre_xor] = freq_map.get(pre_xor, 0) + 1

        return count
