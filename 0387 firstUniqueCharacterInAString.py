"""
字符串中的第一个唯一字符

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 
提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表、字符串
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.firstUniqChar('leetcode')
    print(r)
    r = s.firstUniqChar('loveleetcode')
    print(r)
