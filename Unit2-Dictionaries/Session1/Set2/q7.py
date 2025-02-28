# Problem 7: Signal Pairs
# Ground control is analyzing signal patterns received from different probes. 
# You are given a 0-indexed array signals consisting of distinct strings.

# The string signals[i] can be paired with the string signals[j] if the string 
# signals[i] is equal to the reversed string of signals[j]. 0 <= i < j < len(signals). 
# Return the maximum number of pairs that can be formed from the array signals.

# Note that each string can belong in at most one pair.

def max_number_of_string_pairs(signals):
    seen = set()
    count = 0
    
    for signal in signals:
        reversed_signal = signal[::-1]
        if reversed_signal in seen:
            count += 1
            seen.remove(reversed_signal)
            
        else:
            seen.add(signal)
            
    return count
    

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

print(max_number_of_string_pairs(signals1))
print(max_number_of_string_pairs(signals2))
print(max_number_of_string_pairs(signals3))