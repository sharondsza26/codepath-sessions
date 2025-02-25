# Problem 3: Secret Identity
# Write a function remove_name() to keep Batman's secret identity hidden. 
# The function accepts a list of names people and a string secret_identity and 
# should return the list with any instances of secret_identity removed. The list must be modified in place;
# you may not create any new lists as part of your solution. Relative order of the remaining elements must 
# be maintained.

def remove_name(people, secret_identity):
    while secret_identity in people:
        people.remove(secret_identity)
    return people


people = ['Batman', 'Superman', 'Bruce Wayne', 'The Riddler', 'Bruce Wayne']
secret_identity = 'Bruce Wayne'
print(remove_name(people, secret_identity))
