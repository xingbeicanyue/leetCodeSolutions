"""
最佳买卖股票时机含冷冻期

给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格。
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
* 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
* 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

示例 2:
输入: prices = [1]
输出: 0

提示：
* 1 <= prices.length <= 5000
* 0 <= prices[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        buy, sell, cool = -prices[0], 0, 0  # 当前 买入|卖出|不操作 后的最佳收益
        for i in range(1, len(prices)):
            buy, sell, cool = max(buy, cool - prices[i]), buy + prices[i], max(cool, sell)
        return max(sell, cool)


if __name__ == '__main__':
    s = Solution()

    r = s.maxProfit([1, 2, 3, 0, 2])
    print(r)

    r = s.maxProfit([1])
    print(r)
