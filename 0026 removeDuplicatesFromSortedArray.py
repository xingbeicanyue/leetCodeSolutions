"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。

示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        resultIdx = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[resultIdx]:
                resultIdx += 1
                nums[resultIdx] = nums[i]
        return resultIdx + 1 if len(nums) > 0 else 0


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    r = s.removeDuplicates(nums)
    print(nums, r)
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    r = s.removeDuplicates(nums)
    print(nums, r)
