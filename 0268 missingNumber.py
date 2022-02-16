"""
丢失的数字

给定一个包含 [0, n] 中n个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。

示例 1：
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。

提示：
* n == nums.length
* 1 <= n <= 10^4
* 0 <= nums[i] <= n
* nums 中的所有数字都独一无二

进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：位运算、数组、哈希表、数学、排序
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = len(nums)
        return count * (count + 1) // 2 - sum(nums)


if __name__ == '__main__':
    s = Solution()

    r = s.missingNumber([3, 0, 1])
    print(r)

    r = s.missingNumber([0, 1])
    print(r)

    r = s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
    print(r)

    r = s.missingNumber([0])
    print(r)