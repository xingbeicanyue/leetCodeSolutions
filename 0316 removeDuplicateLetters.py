"""
去除重复字母

给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小
（要求不能打乱其他字符的相对位置）。

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"
 
提示：
* 1 <= s.length <= 104
* s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、贪心算法、字符串
重复题目：#1081
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 收集每个字符最后出现的位置
        charLastPosDic = {c: i for i, c in enumerate(s)}

        # 将不重复的字符依次加入队列中，如果队列非递增，且加入前队列尾元素之后还会出现，则移除之
        collectedChars = set()  # 在队列中出现的字符集合
        digits = []
        for i, c in enumerate(s):
            if c in collectedChars:
                continue
            while digits and c < digits[-1] and charLastPosDic[digits[-1]] > i:
                collectedChars.remove(digits.pop())
            collectedChars.add(c)
            digits.append(c)
        return ''.join(digits)


if __name__ == '__main__':
    s = Solution()
    r = s.removeDuplicateLetters('bcabc')
    print(r)
    r = s.removeDuplicateLetters('cbacdcbc')
    print(r)
