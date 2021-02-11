"""
寻找重复数

给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有一个重复的整数，找出这个重复的数。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3

示例 3：
输入：nums = [1,1]
输出：1

示例 4：
输入：nums = [1,1,2]
输出：1

提示：
* 2 <= n <= 3 * 10^4
* nums.length == n + 1
* 1 <= nums[i] <= n
* nums 中只有一个整数出现两次或多次，其余整数均只出现一次

进阶：
* 如何证明 nums 中至少存在一个重复的数字?
* 你可以在不修改数组 nums 的情况下解决这个问题吗？
* 你可以只用常量级 O(1) 的额外空间解决这个问题吗？
* 你可以设计一个时间复杂度小于 O(n^2) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针、二分查找
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if sum(1 for num in nums if num <= mid) > mid:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    r = s.findDuplicate([1, 3, 4, 2, 2])
    print(r)
    r = s.findDuplicate([3, 1, 3, 4, 2])
    print(r)
    r = s.findDuplicate([1, 1])
    print(r)
    r = s.findDuplicate([1, 1, 2])
    print(r)
