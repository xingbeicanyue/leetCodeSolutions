"""
给定一个增序排列数组 nums ，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。
     你不需要考虑数组中超出新长度后面的元素。

提示：
* 0 <= nums.length <= 3 * 10^4
* -10^4 <= nums[i] <= 10^4
* nums 按递增顺序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        resultIdx, duplicate = 0, False
        for i in range(1, len(nums)):
            isSame = nums[i] == nums[resultIdx]
            if not (isSame and duplicate):
                resultIdx += 1
                nums[resultIdx], duplicate = nums[i], isSame
        return resultIdx + 1 if len(nums) else 0


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    r = s.removeDuplicates(nums)
    print(nums, r)
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    r = s.removeDuplicates(nums)
    print(nums, r)
