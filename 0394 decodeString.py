"""
字符串解码

给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"

示例 3：
输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

示例 4：
输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、深度优先搜索
"""


class Solution:
    def decodeString(self, s: str) -> str:

        def parse() -> str:
            """ 从idx开始解析一层字符串 """
            nonlocal idx
            result = []
            while idx < len(s):
                if s[idx].isdigit():  # 解析下一层
                    digitSPos, digitEPos = idx, s.find('[', idx)
                    idx = digitEPos + 1
                    result.append(parse() * int(s[digitSPos: digitEPos]))
                elif s[idx] == ']':  # 本层解析结束
                    break
                else:
                    result.append(s[idx])
                idx += 1
            return ''.join(result)

        idx = 0
        return parse()


if __name__ == '__main__':
    s = Solution()
    r = s.decodeString('3[a]2[bc]')
    print(r)
    r = s.decodeString('3[a2[c]]')
    print(r)
    r = s.decodeString('2[abc]3[cd]ef')
    print(r)
    r = s.decodeString('abc3[cd]xyz')
    print(r)
