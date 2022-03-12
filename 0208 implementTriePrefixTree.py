"""
实现 Trie (前缀树)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true

说明:
* 你可以假设所有的输入都是由小写字母 a-z 构成的。
* 保证所有输入均为非空字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Trie:

    def __init__(self):
        self._root = {}

    def insert(self, word: str) -> None:
        curNode = self._root
        for c in word:
            curNode = curNode.setdefault(c, {})
        curNode['0'] = {}  # 用'0'表示字符串结束

    def search(self, word: str) -> bool:
        curNode = self._root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return '0' in curNode

    def startsWith(self, prefix: str) -> bool:
        curNode = self._root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return True


if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    print(trie.search('apple'))
    print(trie.search('app'))
    print(trie.startsWith('app'))
    trie.insert('app')
    print(trie.search('app'))
