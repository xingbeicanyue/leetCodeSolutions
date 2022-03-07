"""
找到所有数组中消失的数字

给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。
请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

示例 1：
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

示例 2：
输入：nums = [1,1]
输出：[2]

提示：
* n == nums.length
* 1 <= n <= 10^5
* 1 <= nums[i] <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 用数组当作哈希表，遍历时遇到数字i，就把对应下标i-1的数字+n，表示该数字出现过
        # 注意遍历时的数字可能已经被修改过，需要对n取模
        length = len(nums)
        for i, num in enumerate(nums):
            nums[num % length - 1] += length  # 下标可能为-1，正好是合理的
        return [i + 1 for i, num in enumerate(nums) if num <= length]


if __name__ == '__main__':
    s = Solution()

    r = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(r)

    r = s.findDisappearedNumbers([1, 1])
    print(r)
