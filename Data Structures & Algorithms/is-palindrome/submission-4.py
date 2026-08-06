class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleaned)-1
        while left < right:
            if cleaned[left] == cleaned[right]:
                print(cleaned[left])
                left += 1
                right -= 1
            else:
                return False
        return True