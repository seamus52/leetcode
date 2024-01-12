public class TrieNode
{
    public char? c;
    public Dictionary<char, TrieNode> children;
    public bool is_word;

    public TrieNode(char c='/') // '/' formally designates root
    {
        this.c = c;
        this.children = new();
        this.is_word = false;
    }
}

public class Trie
{
    private TrieNode root;

    public Trie()
    {
        root = new();
    }
    
    public void Insert(string word)
    {
        var node = this.root;
        foreach(char c in word)
        {
            if (!node.children.ContainsKey(c)) {
                node.children[c] = new TrieNode(c);
            }
            node = node.children[c];
        }
        node.is_word = true;
    }
    
    public bool Search(string word)
    {
        var node = this.root;
        foreach(char c in word)
        {
            if (!node.children.ContainsKey(c)) {
                return false;
            }
            node = node.children[c];
        }
        
        return node.is_word;
    }
    
    public bool StartsWith(string prefix)
    {
        var node = this.root;
        foreach(char c in prefix)
        {
            if (!node.children.ContainsKey(c)) {
                return false;
            }
            node = node.children[c];
        }
        
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.Insert(word);
 * bool param_2 = obj.Search(word);
 * bool param_3 = obj.StartsWith(prefix);
 */
