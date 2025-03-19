def isPalindrome(s):
    return s.lower() == s.lower()[::-1]
    # My previous code:
    #   copy = s[::-1]
    #   if copy == s: return True
    #   else: return False

string = input('Enter a string: ')
if isPalindrome(string): print('Is palindrome')
else: print('Is not palindrome')