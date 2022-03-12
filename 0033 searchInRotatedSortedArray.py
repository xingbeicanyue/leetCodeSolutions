"""
搜索旋转排序数组

升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：
输入：nums = [1], target = 0
输出：-1

提示：
* 1 <= nums.length <= 5000
* -10^4 <= nums[i] <= 10^4
* nums 中的每个值都独一无二
* nums 肯定会在某个点上旋转
* -10^4 <= target <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        onLeft = target >= nums[0]  # 是否位于左半边
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if onLeft and nums[mid] < nums[0]:
                right = mid - 1
            elif not onLeft and nums[mid] > nums[-1]:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] == target else -1


if __name__ == '__main__':
    s = Solution()
    r = s.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(r)
    r = s.search([4, 5, 6, 7, 0, 1, 2], 3)
    print(r)
    r = s.search([1], 0)
    print(r)
