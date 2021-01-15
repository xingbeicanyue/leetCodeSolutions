"""
最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"

示例 2:
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、动态规划
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        leftRemain = 0  # 未匹配的左括号数
        startPos = 0  # 当前有效字串起始下标
        for i, c in enumerate(s):
            if c == '(':
                leftRemain += 1
            else:
                leftRemain -= 1
                if leftRemain == 0:
                    result = max(result, i - startPos + 1)
                if leftRemain < 0:
                    leftRemain, startPos = 0, i + 1
        if leftRemain > 0:  # 还有未匹配的左括号，在startPos后可能存在有效括号子串，需反向遍历
            rightRemain = 0  # 未匹配的右括号数
            startPos, endPos = len(s) - 1, startPos
            for i in range(len(s) - 1, endPos, -1):
                if s[i] == ')':
                    rightRemain += 1
                else:
                    rightRemain -= 1
                    if rightRemain == 0:
                        result = max(result, startPos - i + 1)
                    if rightRemain < 0:
                        rightRemain, startPos = 0, i - 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.longestValidParentheses('(()')
    print(r)
    r = s.longestValidParentheses(')()())')
    print(r)
