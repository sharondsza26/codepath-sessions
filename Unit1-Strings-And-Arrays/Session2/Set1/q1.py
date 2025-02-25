# Problem 1: Reverse Sentence
# Write a function reverse_sentence() that takes in a string sentence and returns the sentence with 
# the order of the words reversed. The sentence will contain only alphabetic characters and spaces 
# to separate the words. 
# If there is only one word in the sentence, the function should return the original string.


def reverse_sentence(sentence):
    new_str = sentence.split()
    print(new_str)
    
    for i in range(len(new_str)-1, -1, -1):
        print(new_str[i])
    
    
sentence = "tubby little cubby"
reverse_sentence(sentence)