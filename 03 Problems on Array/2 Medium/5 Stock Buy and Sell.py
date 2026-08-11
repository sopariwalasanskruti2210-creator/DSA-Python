'''
Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. 
Determine the maximum profit achievable by buying and selling the stock at most once. 
The stock should be purchased before selling it, and both actions cannot occur on the same day.
'''
prices = [7,6,4,3,1]
max_profit=0
min_price = prices[0]
for price in prices:
  if price<min_price:
    min_price=price
    profit=price-min_price
    if profit>max_profit:
      max_profit=profit

print(max_profit)