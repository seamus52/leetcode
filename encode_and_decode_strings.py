# time: O(n) - depends on separator implementation
# space: O(n) encode, O(1) decode
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        separator = "#$@SEPARATOR@$#"
        # print(separator.join(strs))
        return separator.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        separator = "#$@SEPARATOR@$#"
        return s.split(separator)

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
