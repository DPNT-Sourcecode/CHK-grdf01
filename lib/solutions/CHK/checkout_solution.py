

# noinspection PyUnusedLocal
# skus = unicode string

PRICING = {"A": 50, "B": 30, "C": 20, "D": 15}
MULTIBUY_AMOUNTS = {"A": 3, "B": 2}
MULTIBUY_PRICES = {"A": 130, "B": 45}


def checkout(skus):
    product_frequency = basket_products(skus)
    pricing(product_frequency)
    return pricing(product_frequency)


def basket_products(skus):
    freq = {}
    for ch in skus:
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def pricing(items):
    totals = 0
    for n in items:
        if n not in PRICING:
            totals += -1
        elif n == "A" or n == "B":
            totals += multi_buy_discount(n, items[n])
        else:
            totals += PRICING[n] * items[n]
    return totals


def multi_buy_discount(product, amount):
    multibuy = MULTIBUY_AMOUNTS[product]
    discounted_price = MULTIBUY_PRICES[product]
    if product == "A":
        discounted_items = amount // 3
    else:
        discounted_items = amount // 2
    non_discounted_items = amount - (discounted_items * multibuy)
    return (discounted_items*discounted_price)+(non_discounted_items*PRICING[product])


