

def validpanlindrome(s: str) -> bool:
    """a phrase is palindrome if, after converting all
        uppercase letters into lowercase letters and removing all
        non-alphanumeric characters, it reads the same forward and backward.
    
    """
    word  = "".join(char for char in s if char.isalnum()).lower()
    return word ==word[::-1]
            