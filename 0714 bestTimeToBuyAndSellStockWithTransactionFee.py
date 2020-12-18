"""
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
* 0 < prices.length <= 50000.
* 0 < prices[i] < 50000.
* 0 <= fee < 50000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：贪心算法、数组、动态规划
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        result = 0
        low = high = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            high = max(price, high)
            if price <= low or price <= high - fee:  # 当前价格<=本次交易最低价 或 与最高点差价>=手续费时 在最高价卖出
                result += max((high - low - fee), 0)
                low = high = price
        return result + max((high - low - fee), 0)


if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([1, 3, 2, 8, 4, 9], 2)
    print(r)
