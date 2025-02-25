# Problem 12: Shuffle
# Write a function shuffle() that accepts a list cards of 2n elements in 
# the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
    x = 0
    y = (len(cards) // 2 )
    lst = []
    for i in range(len(cards)):
        lst.append(cards[x])
        lst.append(cards[y])
        # temp = cards[x]
        # cards[x] = cards[y]
        # cards[y] = temp
        
        x += 1
        y += 1
        
        if y > len(cards) -1:
            break
        
    print(lst)
    


cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
