"""
找到所有数组中消失的数字

给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i, num in enumerate(nums):
            nums[num % length - 1] += length  # 下标可能为-1，正好是合理的
        return [i + 1 for i, num in enumerate(nums) if num <= length]


if __name__ == '__main__':
    s = Solution()
    r = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(r)
