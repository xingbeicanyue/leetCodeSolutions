"""
基本计算器 II

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1

示例 3：
输入：s = " 3+5 / 2 "
输出：5

提示：
* 1 <= s.length <= 3 * 10^5
* s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
* s 表示一个有效表达式
* 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
* 题目数据保证答案是一个 32-bit 整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def calculate(self, s: str) -> int:

        def parseMD(sIdx, eIdx: int) -> int:
            """ 处理乘除式 或 数字 """
            for i in range(eIdx, sIdx - 1, -1):
                if s[i] == '*':
                    return parseMD(sIdx, i - 1) * int(s[i + 1: eIdx + 1])
                elif s[i] == '/':
                    return parseMD(sIdx, i - 1) // int(s[i + 1: eIdx + 1])
            return int(s[sIdx: eIdx + 1])

        def parseAS(sIdx, eIdx: int) -> int:
            """ 处理加减式 """
            for i in range(eIdx, sIdx - 1, -1):
                if s[i] == '+':
                    return parseAS(sIdx, i - 1) + parseMD(i + 1, eIdx)
                elif s[i] == '-':
                    return parseAS(sIdx, i - 1) - parseMD(i + 1, eIdx)
            return parseMD(sIdx, eIdx)

        return parseAS(0, len(s) - 1)


if __name__ == '__main__':
    s = Solution()

    r = s.calculate('3+2*2')
    print(r)

    r = s.calculate(' 3/2 ')
    print(r)

    r = s.calculate(' 3+5 / 2 ')
    print(r)
