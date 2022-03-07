"""
有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
* 左括号必须用相同类型的右括号闭合。
* 左括号必须以正确的顺序闭合。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true

提示：
* 1 <= s.length <= 10^4
* s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、字符串
"""


class Solution:
    _parenthesisDic = {')': '(', ']': '[', '}': '{', '?': '?'}

    def isValid(self, s: str) -> bool:
        leftParenthesis = ['?']  # 哨兵，当访问到"?"则表示右括号多于左括号
        for c in s:
            if c in Solution._parenthesisDic:
                if leftParenthesis.pop() != Solution._parenthesisDic[c]:
                    return False
            else:
                leftParenthesis.append(c)
        return len(leftParenthesis) == 1


if __name__ == '__main__':
    s = Solution()

    r = s.isValid('()')
    print(r)

    r = s.isValid('()[]{}')
    print(r)

    r = s.isValid('(]')
    print(r)

    r = s.isValid('([)]')
    print(r)

    r = s.isValid('{[]}')
    print(r)
