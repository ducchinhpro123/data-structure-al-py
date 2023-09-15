def buy_and_sell_stock_once(prices):
    profit_max = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > profit_max:
                profit_max = prices[j] - prices[i]

    return profit_max


def buy_and_sell_stock_once_2(prices):
    min_prices = 10000000
    max_profit = 0
    for price in prices:
        min_prices = min(min_prices, price)
        selling = price - min_prices
        max_profit = max(selling, max_profit)
    return max_profit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stock_once_2(prices=prices))
