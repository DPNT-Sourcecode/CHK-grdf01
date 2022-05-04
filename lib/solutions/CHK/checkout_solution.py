

# noinspection PyUnusedLocal
# skus = unicode string

PRICING = {"A": 50, "B": 30, "C": 20, "D": 15}


def checkout(skus):
    return PRICING[skus]


