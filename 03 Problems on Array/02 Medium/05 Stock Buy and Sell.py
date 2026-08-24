"""
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock at most once.
The stock should be purchased before selling it, and both actions cannot occur on the same day.
"""

prices = [7, 6, 1, 3, 5]
max_profit = 0
min_price = prices[0]

for price in prices:

    # Check if current price is min then prev one
    if price < min_price:
        min_price = price

    else:
        # Calculate the profit
        profit = price - min_price

        # If profit is greater than prev than update the max_profit
        if profit > max_profit:
            max_profit = profit

print(max_profit)
