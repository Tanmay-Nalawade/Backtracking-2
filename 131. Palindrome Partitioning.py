class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.helper(s, 0, [])
        return self.result
    def helper(self, s, pivot, path):
        def is_palindrome(s, start, end):
            if s == s[:: -1]:
                return True
            return False
        # Base case
        if pivot == len(s):
            self.result.append(list(path))

        # Logic
        for i in range(pivot, len(s)):
            curr_path = s[pivot: i + 1: 1]
            if is_palindrome(curr_path, 0, len(curr_path)):
                # Action
                path.append(curr_path)
                # Recurse
                self.helper(s, i + 1, path)
                # Backtrack
                path.pop()