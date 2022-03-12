"""
戳气球

有 n 个气球，编号为 0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 
这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
求所能获得硬币的最大数量。

示例 1：
输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

示例 2：
输入：nums = [1,5]
输出：10

提示：
* n == nums.length
* 1 <= n <= 500
* 0 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/burst-balloons
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 动态规划：
        # 在[a, b]中分别以每个气球为最后一个戳破的气球，求所有情况中的最大值
        # 即nums[a, b]的最大硬币数为 max(nums[a,k-1] + nums[k+1,b] + nums[k]*nums[a-1]*nums[b+1]) (a<=k<=b)
        nums = [1] + nums + [1]
        length = len(nums)
        maxCoinsTable = [[0] * length for _ in range(length)]
        for i in range(1, length - 1):  # 每轮计算长度为i的每个区间的最大硬币
            for j in range(1, length - i):  # 每轮计算区间[j, j+i-1]的最大硬币
                # 每轮计算k最后一个戳的情况下的最大硬币
                maxCoinsTable[j][j + i - 1] = max(maxCoinsTable[j][k - 1] + maxCoinsTable[k + 1][j + i - 1] +
                                                  nums[k] * nums[j - 1] * nums[j + i] for k in range(j, j + i))
        return maxCoinsTable[1][length - 2]


if __name__ == '__main__':
    s = Solution()
    r = s.maxCoins([3, 1, 5, 8])
    print(r)
    r = s.maxCoins([1, 5])
    print(r)
