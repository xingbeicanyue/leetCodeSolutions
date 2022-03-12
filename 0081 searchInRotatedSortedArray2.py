"""
搜索旋转排序数组 II

假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组[0,0,1,2,2,5,6]可能变为[2,5,6,0,0,1,2])。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回true，否则返回false。

示例 1:
输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true

示例 2:
输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false

进阶:
* 这是 #33 搜索旋转排序数组的延伸题目，本题中的 nums 可能包含重复元素。
* 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        if target == nums[0] or target == nums[-1]:
            return True
        onLeft = target > nums[0]
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if onLeft:
                if nums[mid] == nums[left]:  # 无法区分mid在左还是在右，缓慢缩小边界
                    left += 1
                elif nums[mid] < nums[left] or nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] == nums[right]:  # 无法区分mid在左还是在右，缓慢缩小边界
                    right -= 1
                elif nums[mid] > nums[right] or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return nums[left] == target


if __name__ == '__main__':
    s = Solution()

    r = s.search([2, 5, 6, 0, 0, 1, 2], 0)
    print(r)

    r = s.search([2, 5, 6, 0, 0, 1, 2], 3)
    print(r)
