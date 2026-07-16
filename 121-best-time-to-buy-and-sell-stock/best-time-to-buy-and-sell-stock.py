# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         lowest_buy_price = prices[0]
#         max_profit = 0

#         for current_price in prices[1:]:
#             if(current_price < lowest_buy_price):
#                 lowest_buy_price = current_price
            
#             if(current_price > lowest_buy_price):
#                 profit_today = current_price - lowest_buy_price
#                 max_profit = max(profit_today, max_profit)

#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = prices[0]
        max_profit = 0

        for current_price in prices[1:]:
            lowest_buy_price = min(lowest_buy_price, current_price)

            profit_today = current_price - lowest_buy_price

            max_profit = max(max_profit, profit_today)

        return max_profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:

#         max_profit = 0

#         for buy_index, buy_price in enumerate(prices[:-1]):
#             sell_price = max(prices[buy_index+1:])

#             if(sell_price > buy_price):
#                 profit = sell_price - buy_price
#                 max_profit = max(profit, max_profit)

#         return max_profit



