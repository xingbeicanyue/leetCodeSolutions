"""
两数之和 II - 输入有序数组

给你一个下标从 1 开始的整数数组 numbers ，该数组已按非递减顺序排列，请你从数组中找出满足相加之和等于目标数 target 的两个数。
如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。

示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

提示：
* 2 <= numbers.length <= 3 * 10^4
* -1000 <= numbers[i] <= 1000
* numbers 按非递减顺序排列
* -1000 <= target <= 1000
* 仅存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from bisect import bisect_right
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 双指针从两端向中间移动
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

    r = s.twoSum([2, 3, 4], 6)
    print(r)

    r = s.twoSum([-1, 0], -1)
    print(r)
