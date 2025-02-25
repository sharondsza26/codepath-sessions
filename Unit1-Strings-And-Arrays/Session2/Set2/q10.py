# Problem 10: Exposing Superman
# Metropolis has a population n, with each citizen assigned an integer id from 1 to n. 
# There's a rumor that Superman is an ordinary citizen among this group.

# If Superman is an ordinary citizen, then:

# Superman trusts nobody.
# Everybody (except for Superman) trusts Superman.
# There is exactly one citizen that satisfies properties 1 and 2.
# Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] 
# representing that the person labeled ai trusts the person labeled bi. 
# If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of Superman if he is hiding amongst the population and can be identified, 
# or return -1 otherwise.

def expose_superman(trust, n):
    trust_count = [0] * (n + 1)  # to count how many times each person is trusted
    trusts_other = [0] * (n + 1)  # to count how many people each person trusts
    
    # Fill the trust_count and trusts_other arrays
    for a, b in trust:
        trusts_other[a] += 1  # person a trusts someone
        trust_count[b] += 1    # person b is trusted by someone
    
    # Find the person who is trusted by everyone and trusts nobody
    for i in range(1, n + 1):
        if trust_count[i] == n - 1 and trusts_other[i] == 0:
            return i  # This person is Superman
    
    return -1  # No such person exists

n = 2
trust = [[1, 2]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3]]
print(expose_superman(trust, n))

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
print(expose_superman(trust, n))
