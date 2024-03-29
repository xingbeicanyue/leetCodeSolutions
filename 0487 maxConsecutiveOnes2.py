"""
最大连续1的个数 II

给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

示例 1：
输入：[1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。

注：
* 输入数组只包含 0 和 1.
* 输入数组的长度为正整数，且不超过 10,000

进阶：
如果输入的数字是作为无限流逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, sIdx, lastZeroPos = 1, 0, -1
        for i, num in enumerate(nums):
            if num == 0:
                result = max(result, i - sIdx)
                sIdx, lastZeroPos = lastZeroPos + 1, i
        return max(result, len(nums) - sIdx)


if __name__ == '__main__':
    s = Solution()
    r = s.findMaxConsecutiveOnes([1, 0, 1, 1, 0])
    print(r)
