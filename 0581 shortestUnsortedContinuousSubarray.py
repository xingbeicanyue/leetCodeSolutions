"""
最短无序连续子数组

给你一个整数数组 nums ，你需要找出一个连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的最短子数组，并输出它的长度。

示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

示例 2：
输入：nums = [1,2,3,4]
输出：0

示例 3：
输入：nums = [1]
输出：0

提示：
* 1 <= nums.length <= 10^4
* -10^5 <= nums[i] <= 10^5

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 正向遍历，最后一个小于当前最大值的下标为右边界
        # 反向遍历，最后一个大于当前最小值的下标为左边界
        minVal, maxVal = 100001, -100001
        leftIdx = rightIdx = -1
        for i, num in enumerate(nums):
            if num < maxVal:
                rightIdx = i
            else:
                maxVal = num
        for i, num in enumerate(reversed(nums)):  # 左边界为 len(nums) - 1 - leftIdx
            if num > minVal:
                leftIdx = i
            else:
                minVal = num
        return rightIdx + leftIdx + 2 - len(nums) if leftIdx >= 0 else 0


if __name__ == '__main__':
    s = Solution()
    r = s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
    print(r)
    r = s.findUnsortedSubarray([1, 2, 3, 4])
    print(r)
    r = s.findUnsortedSubarray([1])
    print(r)
