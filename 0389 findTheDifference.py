"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：
输入：s = "", t = "y"
输出："y"

示例 3：
输入：s = "a", t = "aa"
输出："a"

示例 4：
输入：s = "ae", t = "aea"
输出："a"

提示：
* 0 <= s.length <= 1000
* t.length == s.length + 1
* s 和 t 只包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：位运算、哈希表
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from functools import reduce
        return chr(reduce(lambda x, y: x ^ ord(y), s + t, 0))


if __name__ == '__main__':
    s = Solution()
    r = s.findTheDifference('abcd', 'abcde')
    print(r)
    r = s.findTheDifference('', 'y')
    print(r)
    r = s.findTheDifference('a', 'aa')
    print(r)
    r = s.findTheDifference('ae', 'aea')
    print(r)
