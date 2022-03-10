"""
每日温度

给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指在第 i 天之后，才会有更高的温度。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]

提示：
* 1 <= temperatures.length <= 10^5
* 30 <= temperatures[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、数组、单调栈
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        lowTempIdxs = []  # 维护对应温度递减的日期栈：stack[日期]
        for i, temp in enumerate(temperatures):
            while lowTempIdxs and temp > temperatures[lowTempIdxs[-1]]:  # 依次将栈中小于当前温度的日期填入天数差
                date = lowTempIdxs.pop()
                result[date] = i - date
            lowTempIdxs.append(i)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print(r)

    r = s.dailyTemperatures([30, 40, 50, 60])
    print(r)

    r = s.dailyTemperatures([30, 60, 90])
    print(r)
