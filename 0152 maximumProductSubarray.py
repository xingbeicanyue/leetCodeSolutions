"""
乘积最大子数组

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、动态规划
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # 下面的动态规划不适用于nums只有一个数且该数为负的情况
        result, maxPositive, maxNegative = nums[0], 0, 0
        for num in nums:
            if num >= 0:
                maxPositive, maxNegative = (maxPositive or 1) * num, maxNegative * num
            else:
                maxPositive, maxNegative = maxNegative * num, (maxPositive or 1) * num
            result = max(result, maxPositive)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxProduct([2, 3, -2, 4])
    print(r)
    r = s.maxProduct([-2, 0, -1])
    print(r)
