class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        i = len(words)
        for j in range(0, i):
            if (words[j][::-1]) == (words[j]):
                return (words[j])
        return ""
