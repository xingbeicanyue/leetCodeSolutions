"""
强整数

给定三个整数 x 、 y 和 bound ，返回值小于或等于 bound 的所有强整数组成的列表 。
如果某一整数可以表示为 xi + yj ，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

示例 1：
输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释：
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2

示例 2：
输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]

提示：
* 1 <= x, y <= 100
* 0 <= bound <= 10^6
"""

from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        def getPowers(value: int) -> List[int]:
            """ 返回value的i次幂列表 """
            if value == 1:
                return [1]
            result = []
            curVal = 1
            while curVal < bound:
                result.append(curVal)
                curVal *= value
            return result

        xs, ys = getPowers(x), getPowers(y)
        result = set()
        for curX in xs:
            for curY in ys:
                if curX + curY <= bound:
                    result.add(curX + curY)
                else:
                    break
        return list(result)


if __name__ == '__main__':
    s = Solution()

    print(s.powerfulIntegers(2, 3, 10))

    print(s.powerfulIntegers(3, 5, 15))
