class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        words = s.split(" ")
        words = [s[::-1] for s in words]
        return " ".join(words)
        