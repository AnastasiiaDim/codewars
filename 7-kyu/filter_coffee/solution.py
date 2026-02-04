def search(budget, prices):
    result = []
    for price in prices:
        if price <= budget:
            result.append(price)

    result.sort()

    return ",".join(map(str, result))

# affordable = sorted([p for p in prices if p <= budget])
# return ",".join(map(str,affordable))