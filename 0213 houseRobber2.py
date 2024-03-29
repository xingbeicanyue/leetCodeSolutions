"""
打家劫舍 II

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：
输入：nums = [0]
输出：0

提示：
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        def maxValue(sIdx: int, eIdx: int):
            """ 计算nums[sIdx:eIdx]中偷窃的最高金额 """
            robMax, notRobMax = 0, 0
            for i in range(sIdx, eIdx):
                robMax, notRobMax = notRobMax + nums[i], max(robMax, notRobMax)
            return max(robMax, notRobMax)

        if len(nums) == 1:
            return nums[0]
        return max(maxValue(0, len(nums) - 1), maxValue(1, len(nums)))


if __name__ == '__main__':
    s = Solution()
    r = s.rob([2, 3, 2])
    print(r)
    r = s.rob([1, 2, 3, 1])
    print(r)
    r = s.rob([0])
    print(r)
