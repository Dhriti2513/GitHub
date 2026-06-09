class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0

        prefix_map = {0: -1}

        current_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p

            needed = (current_sum - target + p) % p

            if needed in prefix_map:
                min_len = min(min_len, i - prefix_map[needed])

            prefix_map[current_sum] = i

        return min_len if min_len < len(nums) else -1