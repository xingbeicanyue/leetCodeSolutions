"""
在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]

提示：
* 0 <= nums.length <= 10^5
* -10^9 <= nums[i] <= 10^9
* nums 是一个非递减数组
* -10^9 <= target <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = bisect_left(nums, target), bisect_right(nums, target) - 1
        if left == len(nums) or nums[left] != target:
            left = -1
        if right == -1 or nums[right] != target:
            right = -1
        return [left, right]


if __name__ == '__main__':
    s = Solution()

    r = s.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(r)

    r = s.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(r)

    r = s.searchRange([], 0)
    print(r)
