def calculate_change(coins, amount):
    coins.sort(reverse=True)
    change = []
    for coin in coins:
        while amount >= coin:
            change.append(coin)
            amount -= coin
    return change

# Example usage
british_coins = [1, 2, 5, 10, 20, 50]
us_coins = [1, 5, 10, 25]
norwegian_coins = [1, 5, 10, 20]

amount = 43
british_change = calculate_change(british_coins, amount)
us_change = calculate_change(us_coins, amount)
norwegian_change = calculate_change(norwegian_coins, amount)

print("British change:", british_change)
print("US change:", us_change)
print("Norwegian change:", norwegian_change)