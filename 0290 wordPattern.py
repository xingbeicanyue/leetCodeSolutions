"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false

示例 3:
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false

示例 4:
输入: pattern = "abba", str = "dog dog dog dog"
输出: false

说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        patterns, usedWords = [None] * 26, set()
        ordA = ord('a')
        for i, p in enumerate(pattern):
            pOrd = ord(p) - ordA
            if patterns[pOrd] is None:
                if words[i] in usedWords:
                    return False
                patterns[pOrd] = words[i]
                usedWords.add(words[i])
            elif words[i] != patterns[pOrd]:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.wordPattern('abba', 'dog cat cat dog')
    print(r)
    r = s.wordPattern('abba', 'dog cat cat fish')
    print(r)
    r = s.wordPattern('aaaa', 'dog cat cat dog')
    print(r)
    r = s.wordPattern('abba', 'dog dog dog dog')
    print(r)
