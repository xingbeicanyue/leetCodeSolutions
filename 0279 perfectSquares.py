"""
完全平方数

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的最少数量。

完全平方数是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
* 1 <= n <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # 将n拆分为a+b，a为完全平方数，然后继续对b拆分
        # 由于一个数字有多种拆分方式，把每一种拆分方式作为一条路径进行广度优先遍历
        # 最先拆分使b=0时即为最快的拆分方式
        squares = [i * i for i in range(int(n ** 0.5) + 1)]
        lefts, visiteds = [n], set()
        for i in range(n + 1):
            nexts = []
            for left in lefts:
                for square in squares:
                    num = left - square
                    if num == 0:
                        return i + 1
                    if num < 0:
                        break
                    if num not in visiteds:
                        nexts.append(num)
                        visiteds.add(num)
            lefts = nexts


if __name__ == '__main__':
    s = Solution()

    r = s.numSquares(12)
    print(r)

    r = s.numSquares(13)
    print(r)
