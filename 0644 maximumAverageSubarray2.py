"""
子数组最大平均数 II

给你一个包含 n 个整数的数组，请你找出长度大于等于 k 且含最大平均值的连续子数组。并输出这个最大平均值。

示例：
输入：[1,12,-5,-6,50,3], k = 4
输出：12.75
解释：
当长度为 4 的时候，最大平均值是 12.75，
当长度为 5 的时候，最大平均值是 10.8，
当长度为 6 的时候，最大平均值是 9.16667。
所以返回值是 12.75。

提示：
* 1 <= k <= n <= 10,000。
* 数组中的元素范围是 [-10,000, 10,000]。
* 答案的计算误差小于 10^-5 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subarray-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = min(nums), max(nums)
        firstKSum = sum(nums[:k])
        while right - left >= 1e-5:
            midVal = (left + right) / 2
            # 检查是否有连续子串平均数>=midVal
            sumI = firstKSum - midVal * k  # nums前i项和，减去midVal后判断>=0等价于判断平均数>=midVal
            if sumI >= 0:
                left = midVal
                continue
            sumK = minSumK = 0  # nums前i-k项和 | 前n项和最小值(n<=i-k)
            for i in range(k, len(nums)):
                sumI += nums[i] - midVal
                sumK += nums[i - k] - midVal
                minSumK = min(minSumK, sumK)
                if sumI >= minSumK:
                    left = midVal
                    break
            else:
                right = midVal
        return (left + right) / 2


if __name__ == '__main__':
    s = Solution()
    r = s.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
    print(r)
