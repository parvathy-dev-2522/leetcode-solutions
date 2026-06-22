"""
Problem: Two Sum (#1)

Approach:
Use a hashmap to store previously seen numbers and their indices.
For each number, check if target - number exists in the hashmap.

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            # print("Current map:", num_map)
            if complement in num_map:
                return [num_map[complement], i]

            num_map[num] = i


def main():
    nums = [15, 11, 7, 2]
    target = 9

    sol = Solution()
    result = sol.twoSum(nums, target)

    print("Result:", result)


if __name__ == "__main__":
    main()
