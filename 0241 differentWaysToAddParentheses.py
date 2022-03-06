"""
为运算表达式设计优先级

给你一个由数字和运算符组成的字符串 expression，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以按任意顺序返回答案。

示例 1：
输入：expression = "2-1-1"
输出：[0,2]
解释：
((2-1)-1) = 0
(2-(1-1)) = 2

示例 2：
输入：expression = "2*3-4*5"
输出：[-34,-14,-10,-10,10]
解释：
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

提示：
* 1 <= expression.length <= 20
* expression 由数字和算符 '+'、'-' 和 '*' 组成。
* 输入表达式中的所有整数值在范围 [0, 99]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/different-ways-to-add-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：递归、记忆化搜索、数学、字符串、动态规划
"""

from functools import lru_cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache
        def compute(sIdx, eIdx: int) -> List[int]:
            """ 计算expression[sIdx: eIdx]的结果 """
            result = []
            for i in range(sIdx, eIdx):
                if expression[i] in '+-*':
                    left, right = compute(sIdx, i), compute(i + 1, eIdx)
                    if expression[i] == '+':
                        result.extend(i + j for i in left for j in right)
                    elif expression[i] == '-':
                        result.extend(i - j for i in left for j in right)
                    else:
                        result.extend(i * j for i in left for j in right)
            if not result:
                result.append(int(expression[sIdx: eIdx]))
            return result

        return compute(0, len(expression))


if __name__ == '__main__':
    s = Solution()

    r = s.diffWaysToCompute('2-1-1')
    print(r)

    r = s.diffWaysToCompute('2*3-4*5')
    print(r)
