"""
回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"

示例 2：
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：
* 输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串、动态规划
"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        def explore(left: int, right: int) -> int:
            """ left向左，right向右，返回两者相等的次数 """
            sameCount = 0
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                sameCount += 1
                left -= 1
                right += 1
            return sameCount

        result = length = len(s)
        for i in range(1, len(s) - 1):
            result += explore(i - 1, i + 1)
        for i in range(1, len(s)):
            result += explore(i - 1, i)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.countSubstrings('abc')
    print(r)
    r = s.countSubstrings('aaa')
    print(r)
