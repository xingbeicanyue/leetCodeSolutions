"""
有效数字

有效数字（按顺序）可以分成以下几个部分：
1. 一个小数或者整数
2. （可选）一个 'e' 或 'E' ，后面跟着一个整数

小数（按顺序）可以分成以下几个部分：
1.（可选）一个符号字符（'+' 或 '-'）
2. 下述格式之一：
    1. 至少一位数字，后面跟着一个点 '.'
    2. 至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
    3. 一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
1. （可选）一个符号字符（'+' 或 '-'）
2. 至少一位数字

部分有效数字列举如下：
* ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：
* ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个有效数字，请返回 true 。

示例 1：
输入：s = "0"
输出：true

示例 2：
输入：s = "e"
输出：false

示例 3：
输入：s = "."
输出：false

示例 4：
输入：s = ".1"
输出：true

提示：
* 1 <= s.length <= 20
* s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from functools import reduce
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        # 方法1：正则表达式
        pattern = re.compile(r'^[+-]?(\d+\.?|\d*\.\d+)([eE][+-]?\d+)?$')
        return re.match(pattern, s) is not None

        # 方法2：分治
        # 找到e所在位置，检查左侧是否浮点数（不带e）或整数，右侧是否整数
        # 检查浮点数（不带e）：检查符号，找到小数点，左右两侧分别检查是否都是数字
        # 检查整数：检查符号，检查是否都是数字
        # def checkDigit(s: str) -> bool:
        #     """ 检查s是否都是数字 """
        #     return reduce(lambda x, y: x and y.isdigit(), s, True)
        #
        # def checkInteger(sIdx: int, eIdx: int) -> bool:
        #     """ 检查s[sIdx: eIdx]是否整数 """
        #     if sIdx == eIdx:
        #         return False
        #     sIdx += s[sIdx] in ('+', '-')
        #     return eIdx > sIdx and checkDigit(s[sIdx: eIdx])
        #
        # def checkNumber(sIdx: int, eIdx: int) -> bool:
        #     """ 检查s[sIdx: eIdx]是否整数或浮点数 """
        #     if sIdx == eIdx:
        #         return False
        #     dotPos = s[sIdx: eIdx].find('.')
        #     sIdx += s[sIdx] in ('+', '-')
        #     if dotPos >= 0:
        #         if eIdx - sIdx <= 1:  # 长度<=1不可能是浮点数，排除只有一个小数点的情况
        #             return False
        #         return checkDigit(s[sIdx: dotPos]) and checkDigit(s[dotPos + 1: eIdx])
        #     return eIdx > sIdx and checkDigit(s[sIdx: eIdx])
        #
        # ePos = s.upper().find('E')
        # if ePos >= 0:
        #     return checkNumber(0, ePos) and checkInteger(ePos + 1, len(s))
        # return checkNumber(0, len(s))


if __name__ == '__main__':
    s = Solution()

    r = s.isNumber('0')
    print(r)

    r = s.isNumber('e')
    print(r)

    r = s.isNumber('.')
    print(r)

    r = s.isNumber('.1')
    print(r)
