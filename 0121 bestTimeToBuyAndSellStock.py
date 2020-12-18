"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、动态规划
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, acc = 0, 0
        for i in range(1, len(prices)):
            acc += prices[i] - prices[i - 1]
            acc = max(acc, 0)
            result = max(acc, result)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxProfit([7, 1, 5, 3, 6, 4])
    print(r)
    r = s.maxProfit([7, 6, 4, 3, 1])
    print(r)
