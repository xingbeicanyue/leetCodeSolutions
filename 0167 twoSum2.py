"""
给定一个已按照升序排列的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1, 2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针、二分查找
"""

from bisect import bisect_right
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 通过二分查找通常可以提速，注意存在相同元素的情况
        leftIdx, rightIdx = 0, min(len(numbers) - 1, bisect_right(numbers, target - numbers[0]))
        while leftIdx < rightIdx:
            sum_ = numbers[leftIdx] + numbers[rightIdx]
            if sum_ < target:
                leftIdx += 1
            elif sum_ > target:
                rightIdx -= 1
            else:
                return [leftIdx + 1, rightIdx + 1]
        return []


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 15], 9)
    print(r)
