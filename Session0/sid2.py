def longest_palindromic_substring(s):
    if not s:
        return "None"

    start, max_length = 0, 0
    result = ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  # Return valid indices

    for i in range(len(s)):
        # Check odd-length palindromes
        l1, r1 = expand_around_center(i, i)
        # Check even-length palindromes
        l2, r2 = expand_around_center(i, i + 1)

        # Update max palindrome found
        if r1 - l1 > max_length:
            start, max_length = l1, r1 - l1
            result = s[start:start + max_length + 1]
        if r2 - l2 > max_length:
            start, max_length = l2, r2 - l2
            result = s[start:start + max_length + 1]

    return result if max_length > 0 else "None"

# Input handling
inputStr = input().strip()  # Read the input string

# Output the longest palindromic substring or None
print(longest_palindromic_substring(inputStr))
