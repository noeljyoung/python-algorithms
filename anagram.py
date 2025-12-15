class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for char in s:
            if char in s1.keys():
                s1[char] += s1[char] + 1
            else:
                s1[char] = 1
                
        for char in t:
            if char in s2.keys():
                s2[char] += s2[char] + 1
            else:
                s2[char] = 1
                
        return s1 == s2

sol = Solution()
print(sol.is_anagram('anagram', 'nagaram1'))