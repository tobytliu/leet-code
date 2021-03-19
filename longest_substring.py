class Solution:
    def check_no_repeats(self, s: str) -> bool:
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                return False
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        result = 0
        curr_length = 0
        history = {}
        while i + curr_length <= len(s):
            while i + curr_length <= len(s):
                print(history.get(s[i:i+curr_length]))
                if history.get(s[i:i+curr_length]):
                    continue
                # print(f"s[{i}:{curr_length}] = {s[i:i+curr_length]}, {self.check_no_repeats(s[i:i+curr_length])}")
                if self.check_no_repeats(s[i:i+curr_length]):
                    if curr_length > result:
                        result = curr_length
                curr_length += 1
                history[s[i:i+curr_length]] = 1
            curr_length = result + 1
            i += 1
        # print(len(s), result)
        return result

s = "abcabcbb"
foo = Solution()
print(foo.lengthOfLongestSubstring(s))
