# Problem 4: Booby Trap
# Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. 
# The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the 
# trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every 
# letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one 
# letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to 
# balance the pirate code. Given a 0-indexed string code consisting of only lowercase English letters, 
# write a function is_balanced() that returns True if it's possible to remove one letter so that the 
# frequency of all remaining letters is equal, and False otherwise.

def is_balanced(code):
    code_freq = {}
    for i in code:
        code_freq[i] = code_freq.get(i, 0) + 1
        
    freqs = list(code_freq.values())
    print(code_freq)
    print(freqs)
    
    counter = {}
    for freq in freqs:
        counter[freq] = counter.get(freq, 0) + 1
    
    
    if len(counter) == 2:
        # Two distinct frequencies
        (freq1, count1), (freq2, count2) = counter.items()
        
        # Case 1: One frequency is 1, and it occurs only once (can remove that character)
        if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1) :
            return True
        
        if abs(freq1 - freq2) == 1:
            if count1 == 1 or count2 == 1:
                return True
            
    return False
    
    

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 