"""
破坏回文串

给你一个回文字符串 palindrome ，请你将其中一个字符用任意小写英文字母替换，使得结果字符串的字典序最小，且不是回文串。
请你返回结果字符串。如果无法做到，则返回一个空串。

示例 1：
输入：palindrome = "abccba"
输出："aaccba"

示例 2：
输入：palindrome = "a"
输出：""

提示：
* 1 <= palindrome.length <= 1000
* palindrome 只包含小写英文字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/break-a-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <= 1:
            return ''
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome.replace(palindrome[i], 'a', 1)
        return palindrome[:-1] + 'b'


if __name__ == '__main__':
    s = Solution()
    r = s.breakPalindrome('abccba')
    print(r)
    r = s.breakPalindrome('a')
    print(r)
