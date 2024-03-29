"""
最大连续1的个数 III

给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。

示例 1：
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1*,1,1,1,1,1*]
星号位置的数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1*,1*,1,1,1,1*,1,1,0,0,0,1,1,1,1]
星号位置的数字从 0 翻转到 1，最长的子数组长度为 10。

提示：
* 1 <= A.length <= 20000
* 0 <= K <= A.length
* A[i] 为 0 或 1 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        # 滑动窗口获取[连续1的数量] -> ones
        ones, left = [], 0
        for right, num in enumerate(A):
            if num == 0:
                ones.append(right - left)
                left = right + 1
        ones.append(len(A) - left)
        # 再次滑动窗口获取ones中的最大子列表和
        K += 1
        if K >= len(ones):
            return len(A)
        result = curSum = sum(ones[:K])
        for right in range(K, len(ones)):
            curSum += (ones[right] - ones[right - K])
            result = max(result, curSum)
        return result + K - 1


if __name__ == '__main__':
    s = Solution()
    r = s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
    print(r)
    r = s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3)
    print(r)
