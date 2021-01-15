"""
绝对差不超过限制的最长连续子数组

给你一个整数数组 nums ，和一个表示限制的整数 limit，
请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。

示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。

示例 2：
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

示例 3：
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3

提示：
* 1 <= nums.length <= 10^5
* 1 <= nums[i] <= 10^9
* 0 <= limit <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、Sliding Window
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 滑动窗口，同时维护最大值和最小值两个栈
        # 当超出limit时，调整栈的位置
        # 时间复杂度：O(n)
        result, sIdx = 0, 0
        bigStack, smallStack = [0], [0]  # 最大|小值下标栈（递减|增）
        bigIdx, smallIdx = 0, 0  # 栈的起始下标，在此之前的数据为废弃数据（避免克隆数据）
        for i in range(1, len(nums)):
            num = nums[i]
            if num > nums[bigStack[bigIdx]]:
                if num - nums[smallStack[smallIdx]] > limit:
                    result = max(result, i - sIdx)
                    while smallIdx < len(smallStack) and num - nums[smallStack[smallIdx]] > limit:
                        smallIdx += 1
                    sIdx = smallStack[smallIdx - 1] + 1
                smallStack.append(i)
                bigStack, bigIdx = [i], 0
            elif num < nums[smallStack[smallIdx]]:
                if nums[bigStack[bigIdx]] - num > limit:
                    result = max(result, i - sIdx)
                    while bigIdx < len(bigStack) and nums[bigStack[bigIdx]] - num > limit:
                        bigIdx += 1
                    sIdx = bigStack[bigIdx - 1] + 1
                bigStack.append(i)
                smallStack, smallIdx = [i], 0
            else:
                while bigStack:
                    if num <= nums[bigStack[-1]]:
                        bigStack.append(i)
                        break
                    bigStack.pop()
                while smallStack:
                    if num >= nums[smallStack[-1]]:
                        smallStack.append(i)
                        break
                    smallStack.pop()
        return max(result, len(nums) - sIdx)


if __name__ == '__main__':
    s = Solution()
    r = s.longestSubarray([8, 2, 4, 7], 4)
    print(r)
    r = s.longestSubarray([10, 1, 2, 4, 7, 2], 5)
    print(r)
    r = s.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0)
    print(r)
