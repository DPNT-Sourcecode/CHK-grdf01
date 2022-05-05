

# noinspection PyUnusedLocal
# skus = unicode string

PRICING = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}


def checkout(skus):
    product_frequency = basket_products(skus)
    return pricing(product_frequency)


def basket_products(skus):
    freq = {}
    for ch in skus:
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def pricing(items):
    totals = 0
    items = free_product_check(items)
    for n in items:
        if n not in PRICING:
            return -1
        elif n in ["A", "B"]:
            totals += multi_buy_discount(n, items[n])
        else:
            totals += PRICING[n] * items[n]
    return totals


def free_product_check(items):
    if "E" in items and "B" in items:
        product_e = items.get("E") // 2
        items["B"] = max(items["B"]-product_e, 0)
    if "F" in items:
        product_f = items.get("F") // 3
        items["F"] = max(items["F"]-product_f, 0)
    return items


def multi_buy_discount(product, amount):
    if product == "A":
        five_item_discount_items = amount // 5
        amount = amount - (five_item_discount_items*5)
        three_item_discount_items = amount // 3
        amount = amount - (three_item_discount_items * 3)
        return (five_item_discount_items * 200) + (three_item_discount_items * 130) + (amount * 50)
    else:
        discounted_items = amount // 2
        non_discounted_items = amount - (discounted_items * 2)
        return (discounted_items*45)+(non_discounted_items*PRICING[product])



