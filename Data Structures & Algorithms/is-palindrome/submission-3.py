class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        print(cleaned, cleaned[::-1])
        return True if cleaned == cleaned[::-1] else False