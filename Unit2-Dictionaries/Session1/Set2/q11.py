# Problem 11: Sort Signal Data
# Ground control needs to analyze the frequency of signal data received from different probes. 
# Given an array of integers signals, sort the array in increasing order based on the frequency 
# of the values. If multiple values have the same frequency, sort them in decreasing order. 
# Return the sorted array.

# Below is a buggy or incomplete version of the solution. Identify and fix the bugs in the code. 
# Then, perform a code review and suggest improvements.

def frequency_sort(signals):
    freq = {}
    for signal in signals:
            freq[signal] = freq.get(signal, 0) + 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], - x))

    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

print(frequency_sort(signals1)) 
print(frequency_sort(signals2)) 
print(frequency_sort(signals3))