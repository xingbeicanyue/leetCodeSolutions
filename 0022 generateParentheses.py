"""
括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、回溯算法
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def addOneParenthesis(parenthesis: str, leftSingle: int, leftUnused: int):
            """ 添加一个括号
            :param parenthesis: 括号字符串
            :param leftSingle: 未匹配的左括号数
            :param leftUnused: 未使用的左括号数
            """
            if leftUnused == 0:  # 补足剩余右括号
                parenthesis += ')' * (n * 2 - len(parenthesis))
                result.append(parenthesis)
                return
            addOneParenthesis(parenthesis + '(', leftSingle + 1, leftUnused - 1)
            if leftSingle > 0:
                addOneParenthesis(parenthesis + ')', leftSingle - 1, leftUnused)

        if n <= 0:
            return []
        result = []
        addOneParenthesis('', 0, n)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print(r)
