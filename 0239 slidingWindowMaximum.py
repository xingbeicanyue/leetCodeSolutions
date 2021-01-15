"""
滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]

提示：
* 1 <= nums.length <= 10^5
* -10^4 <= nums[i] <= 10^4
* 1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：堆、Sliding Window
"""

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []  # 严格递减栈
        for i in range(k):
            while stack and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        result = [nums[stack[0]]]
        stackStartIdx = 0  # stack的起始下标，之前的数据是废弃数据
        for i in range(k, len(nums)):
            if stack[stackStartIdx] <= i - k:
                stackStartIdx += 1
            while stackStartIdx < len(stack) and nums[i] >= nums[stack[-1]]:
                stack.pop()
            stack.append(i)
            result.append(nums[stack[stackStartIdx]])
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(r)
    r = s.maxSlidingWindow([1], 1)
    print(r)
    r = s.maxSlidingWindow([1, -1], 1)
    print(r)
    r = s.maxSlidingWindow([9, 11], 2)
    print(r)
    r = s.maxSlidingWindow([4, -2], 2)
    print(r)
