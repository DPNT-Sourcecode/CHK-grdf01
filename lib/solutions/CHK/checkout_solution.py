

# noinspection PyUnusedLocal
# skus = unicode string

PRODUCTS = {
    "A": {1: 50, 3: 130, 5: 200},
    "B": {1: 30, 2: 45},
    "C": {1: 20},
    "D": {1: 15},
    "G": {1: 20},
    "H": {1: 10, 5: 45, 10: 80},
    "I": {1: 35},
    "J": {1: 60},
    "K": {1: 70, 2: 120},
    "L": {1: 90},
    "M": {1: 15},
    "O": {1: 10},
    "P": {1: 50, 5: 200},
    "Q": {1: 30, 3: 80},
    "V": {1: 50, 2: 90, 3: 130},
    "W": {1: 20},
    "E": {1: 40},  # 2E get one B free
    "F": {1: 10},  # 2F get one F free
    "N": {1: 40},  # 3N get one M free
    "R": {1: 50},  # 3R get one Q free
    "U": {1: 40},  # 3U get one U free
}

# buy any 3 of (S,T,X,Y,Z) for 45
MIX_AND_MATCH = {
    "S": {1: 20},
    "T": {1: 20},
    "X": {1: 17},
    "Y": {1: 20},
    "Z": {1: 21},
    "multi_price": 45
}


def checkout(skus) -> int:
    product_totals = product_frequency(skus)
    return pricing(product_totals, skus)


def product_frequency(skus) -> dict:
    freq = {}
    for ch in skus:
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def pricing(products, skus):
    totals = 0
    updated_products = free_product_check(products)
    mix_items = get_mix_and_match_products(skus)
    for product in updated_products:
        if product not in {**PRODUCTS, **MIX_AND_MATCH}:
            return -1
        elif product in PRODUCTS:
            totals += quantity_pricing(PRODUCTS[product].keys(), products[product], product)
        else:
            totals += mix_and_match_pricing(mix_items)
    return totals


def free_product_check(items) -> dict:
    if "E" in items and "B" in items:
        product_e = items.get("E") // 2
        items["B"] = max(items["B"]-product_e, 0)
    if "F" in items:
        product_f = items.get("F") // 3
        items["F"] = max(items["F"]-product_f, 0)
    if "N" in items and "M" in items:
        product_e = items.get("N") // 3
        items["M"] = max(items["M"]-product_e, 0)
    if "R" in items and "Q" in items:
        product_e = items.get("R") // 3
        items["Q"] = max(items["Q"]-product_e, 0)
    if "U" in items:
        product_f = items.get("U") // 4
        items["U"] = max(items["U"]-product_f, 0)
    return items


def quantity_pricing(quantity, value, prod) -> int:
    amount = value
    totals = 0
    for n in reversed(quantity):
        ans = amount // n
        if ans:
            amount -= ans * n
            totals += ans*PRODUCTS[prod][n]
    return totals


def get_mix_and_match_products(skus) -> list:
    return [n for n in skus if n in ["S", "T", "X", "Y", "Z"]]


def mix_and_match_pricing(mix_and_match_list) -> int:
    total = 0
    mix_buy = len(mix_and_match_list) // 3
    if mix_buy:
        total += mix_buy*MIX_AND_MATCH["multi_price"]
    remaining_mix_and_match_products = mix_and_match_list[mix_buy*3:]
    if remaining_mix_and_match_products:
        for n in remaining_mix_and_match_products:
            total += MIX_AND_MATCH[n][1]
    return total




