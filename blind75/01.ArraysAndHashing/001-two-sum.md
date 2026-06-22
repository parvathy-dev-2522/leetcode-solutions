## Traditional approach

For each element:

- Compare it with every other element after it.
- If their sum equals the target, return the indices.

```
class Solution(object):
    def twoSum(self, nums, target):

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):

                if nums[i] + nums[j] == target:
                    return [i, j]

```

```
| Approach    | Time  | Space |
| ----------- | ----- | ----- |
| Brute Force | O(n²) | O(1)  |
| HashMap     | O(n)  | O(n)  |

```

## Better optimized approach:

**_ One-Pass Hash Map_**:
You traverse the array only once.
While traversing:

- Calculate the complement (target - num)
- Check if the complement already exists in the hash map
- If yes → return the indices
- If no → store the current number and its index

```
nums = [15, 11, 7, 2]
target = 9

Current map: {}
Current map: {15: 0}
Current map: {15: 0, 11: 1}
Current map: {15: 0, 11: 1, 7: 2}
Result: [2, 3]
```
