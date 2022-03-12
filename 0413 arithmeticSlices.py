"""
等差数列划分

如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的子数组个数。

子数组是数组中的一个连续序列。

示例 1：
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

示例 2：
输入：nums = [1]
输出：0

提示：
* 1 <= nums.length <= 5000
* -1000 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 相邻元素求差，找到每一段中最长的等差数列，一个长为n的等差数列可拆分为n*(n+1)/2个等差数列，求和即可
        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        result = sameCount = 0
        for i in range(len(diffs) - 1):
            if diffs[i] == diffs[i + 1]:
                sameCount += 1
            else:
                result += (1 + sameCount) * sameCount // 2
                sameCount = 0
        return result + (1 + sameCount) * sameCount // 2


if __name__ == '__main__':
    s = Solution()

    r = s.numberOfArithmeticSlices([1, 2, 3, 4])
    print(r)

    r = s.numberOfArithmeticSlices([1])
    print(r)
