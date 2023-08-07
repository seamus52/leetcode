class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.is_leaf = False
        self.content = ""


class FileSystem:
    def __init__(self):
        self.root = TrieNode("/")
        

    def ls(self, path: str) -> List[str]:
        node = self.root
        for name in path.split("/"):
            if name == "" : continue
            node = node.children[name]
        if node.is_leaf:
            return [node.name]
        else:
            return map(lambda f : f.name, sorted(node.children.values(), key=lambda x : x.name))
                
        
    def mkdir(self, path: str) -> None:
        node = self.root
        for name in path.split("/"):
            if name == "" : continue
            if name not in node.children:
                node.children[name] = TrieNode(name)
            node = node.children[name]
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_items = filePath.split("/")
        path = path_items[:-1]
        file_name = path_items[-1]

        node = self.root
        for name in path:
            if name == "" : continue
            node = node.children[name]

        if file_name not in node.children:
            node.children[file_name] = TrieNode(file_name)
        node.children[file_name].is_leaf = True    
        node.children[file_name].content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        for name in filePath.split("/"):
            if name == "" : continue
            node = node.children[name]
        return node.content
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
