class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = ''
        min_len = float('inf')
        for s in strs:
            word_len = len(s)
            if word_len < min_len:
                min_len_word = s
                min_len = word_len
        
        i = 0
        while i < len(min_len_word):
            for s in strs:
                if s == min_len_word:
                    continue
                elif s[i] != min_len_word[i]:
                    return min_len_word[:i]
            i += 1
        return min_len_word[:i]


        