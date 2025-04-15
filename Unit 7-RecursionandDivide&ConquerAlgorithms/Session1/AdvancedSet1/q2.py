# Problem 2: Reversing Deli Orders
# The deli counter is busy, and orders have piled up. To serve the last customer first, you need to reverse the order of the deli orders. Given a string orders where each individual order is separated by a single space, write a recursive function reverse_orders() that returns a new string with the orders reversed.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def reverse_orders(orders):
    def helper(order_list):
        if not order_list:
            return []
        return [order_list[-1]] + helper(order_list[:-1])
    
    order_list = orders.split(" ")
    helper_list = helper(order_list)
    return " ".join(helper_list)
    
# Example Usage:

print(reverse_orders("Bagel Sandwich Coffee"))
# Example Output:

# Coffee Sandwich Bagel