class Trie:

    def __init__(self):
        self.node = {}

    def insert(self, word: str) -> None:
        cur_node = self.node
        for ch in word:
            if ch not in cur_node:
                cur_node[ch] = {}
            cur_node = cur_node[ch]
        cur_node["END"] = {}
            

    def search(self, word: str) -> bool:        
        cur_node = self.node
        for ch in word:
            if ch not in cur_node:
                return False
            
            cur_node = cur_node[ch]
        return "END" in cur_node
                

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.node
        for ch in prefix:
            if ch not in cur_node:
                return False
            
            cur_node = cur_node[ch]
        return True
