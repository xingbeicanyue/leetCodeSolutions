"""
分割等和子集

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

提示：
* 1 <= nums.length <= 200
* 1 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 方法1：
        # 广度优先遍历
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        target, sums = sum_ // 2, {0}  # 单个子集的和 | {子集能组成的和}
        for num in nums:
            newSums = []
            for i, sum_ in enumerate(sums):
                newSum = sum_ + num
                if newSum == target:
                    return True
                elif newSum < target:
                    newSums.append(newSum)
            sums.update(newSums)
        return False

        # 方法2：
        # 背包问题
        # sum_ = sum(nums)
        # if sum_ % 2 == 1:
        #     return False
        # dp = [True] + [False] * (sum_ // 2)  # 遍历至数字num，可以求和成对应下标的数则为True
        # for num in nums:
        #     for i in range(len(dp) - 1, num - 1, -1):
        #         dp[i] |= dp[i - num]
        # return dp[-1]


if __name__ == '__main__':
    s = Solution()

    r = s.canPartition([1, 5, 11, 5])
    print(r)

    r = s.canPartition([1, 2, 3, 5])
    print(r)
