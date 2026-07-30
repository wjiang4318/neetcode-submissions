class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s.lower() if char.isalnum())
        #print(cleaned_text)
        #print(cleaned_text[::-1])
        return cleaned_text == cleaned_text[::-1]