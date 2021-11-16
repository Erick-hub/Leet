class TrieNode:
    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = []
        
class Trie:

    def __init__(self):
        self.root= TrieNode('*')
        
    def insert(self, word: str) -> None:
        node= self.root
        for char in word:
            found_child=False
            for child in node.children:
                if child.char==char:
                    child.counter+=1
                    node=child
                    found_child=True
                    break
            if not found_child:
                new_node=TrieNode(char)
                node.children.append(new_node)
                node=new_node
        node.is_end=True
        
    def search(self, word: str) -> bool:
        node=self.root
        if not self.root.children: #return false if the root has no children
            return False
        for char in word:
            char_found=False
            for child in node.children:
                if child.char==char:
                    char_found=True
                    node=child
                    break
            if not char_found:
                return False
        if node.is_end==True:
            return True
        else:
            return False
    
    def startsWith(self, prefix: str) -> bool:
        node=self.root
        if not self.root.children: #return false if the root has no children
            return False
        for char in prefix:
            char_found=False
            for child in node.children:
                if child.char==char:
                    char_found=True
                    node=child
                    break
            if not char_found:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)