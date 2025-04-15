# Problem 7: Finding the Longest Winning Streak
# In the kingdom's grand tournament, knights compete in a series of challenges. A knight's performance in the challenge is represented by a string challenges, where a success is represented by an S and each other outcome (like a draw or loss) is represented by an "O". Write a recursive function to find the length of the longest consecutive streak of successful challenges ("S").

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def longest_streak(frames, current_length=0, max_length=0):
    if not frames:
        return max_length
    if frames[0] == "S":
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
        
    return longest_streak(frames[1:], current_length, max_length)
# Example Usage:

print(longest_streak("SSOSSS"))
print(longest_streak("SOSOSOSO"))
# Example Output:

# 3
# 1