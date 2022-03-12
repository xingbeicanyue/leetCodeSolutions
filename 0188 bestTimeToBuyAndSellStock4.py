"""
买卖股票的最佳时机 IV

给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

提示：
* 0 <= k <= 109
* 0 <= prices.length <= 1000
* 0 <= prices[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 动态规划
        # 遍历每天的价格，并维护k*2大小的数组s，数组表示第1~k次买入/卖出后的最佳获利
        # 则若为买入s[i] = max(s[i], s[i] - prices[j])，若为卖出s[i] = max(s[i], s[i] + prices[j]) 其中j为天数
        if k == 0 or len(prices) <= 1:
            return 0
        # [第 idx//2 次买入|卖出的最高收益]
        buySells = [-prices[0] if i % 2 == 0 else 0 for i in range(min(k * 2, len(prices) // 2 * 2))]
        for i in range(1, len(prices)):
            for j in range(len(buySells) - 1, 0, -1):
                buySells[j] = max(buySells[j], buySells[j - 1] + prices[i] * (j % 2 * 2 - 1))
            buySells[0] = max(buySells[0], -prices[i])
        return buySells[-1]


if __name__ == '__main__':
    s = Solution()

    r = s.maxProfit(2, [2, 4, 1])
    print(r)

    r = s.maxProfit(2, [3, 2, 6, 5, 0, 3])
    print(r)
