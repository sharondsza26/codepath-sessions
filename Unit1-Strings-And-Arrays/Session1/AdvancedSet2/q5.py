# Problem 5: Heist
# The legendary outlaw Robin Hood is looking for the target of his next heist. 
# Write a function wealthiest_customer() that accepts an m x n 2D integer matrix accounts 
# where accounts[i][j] is the amount of money the i​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return a list [i, w] where i is the 0-based index of the wealthiest customer and 
# w is the total wealth of the wealthiest customer.

# If multiple customers have the highest wealth, return the index of any customer.

# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

def wealthiest_customer(accounts):
    max_wealth = 0
    wealthiest_index = 0
    
    for i in range(len(accounts)):
        total_wealth = sum(accounts[i])
        
        if total_wealth > max_wealth:
            max_wealth = total_wealth
            wealthiest_index = i
            
    print(f'[{wealthiest_index}, {max_wealth}]')
    return [wealthiest_index, max_wealth]

accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)