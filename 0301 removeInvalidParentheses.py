"""
删除无效的括号

删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:
输入: "()())()"
输出: ["()()()", "(())()"]

示例 2:
输入: "(a)())()"
输出: ["(a)()()", "(a())()"]

示例 3:
输入: ")("
输出: [""]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-invalid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def dfs(idx: int, unmatchedCount: int, removeLeftRemain: int, removeRightRemain: int, curStr: str):
            """ 对删除/不删除s[idx]进行深度优先搜索
            :param idx: 当前处理的字符下标
            :param unmatchedCount: 剩余未匹配的左括号数
            :param removeLeftRemain: 剩余待删除左括号数量
            :param removeRightRemain: 剩余待删除右括号数量
            :param curStr: 遍历至当前的字符串
            """
            if idx == len(s) and removeLeftRemain == removeRightRemain == 0:  # 成功调整至合法
                result.add(curStr + s[idx:])
                return
            if idx + removeLeftRemain + removeRightRemain > len(s) or unmatchedCount < 0:  # 已来不及删除、有多余的右括号
                return
            if s[idx] == '(':
                if removeLeftRemain > 0:
                    dfs(idx + 1, unmatchedCount, removeLeftRemain - 1, removeRightRemain, curStr)
                dfs(idx + 1, unmatchedCount + 1, removeLeftRemain, removeRightRemain, curStr + s[idx])
            elif s[idx] == ')':
                if removeRightRemain > 0:
                    dfs(idx + 1, unmatchedCount, removeLeftRemain, removeRightRemain - 1, curStr)
                dfs(idx + 1, unmatchedCount - 1, removeLeftRemain, removeRightRemain, curStr + s[idx])
            else:
                dfs(idx + 1, unmatchedCount, removeLeftRemain, removeRightRemain, curStr + s[idx])

        # 计算要删除的左|右括号数 -> removeLeftCount, removeRightCount
        removeLeftCount = removeRightCount = 0
        for i, c in enumerate(s):
            if c == '(':
                removeLeftCount += 1
            elif c == ')':
                if removeLeftCount == 0:
                    removeRightCount += 1
                else:
                    removeLeftCount -= 1
        # 对每个字符选择删除/不删除，进行深度优先搜索，最终合法的加入结果集中
        result = set()
        dfs(0, 0, removeLeftCount, removeRightCount, '')
        return list(result)


if __name__ == '__main__':
    s = Solution()
    r = s.removeInvalidParentheses('()())()')
    print(r)
    r = s.removeInvalidParentheses('(a)())()')
    print(r)
    r = s.removeInvalidParentheses(')(')
    print(r)
