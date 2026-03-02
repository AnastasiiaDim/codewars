def fridge_organizer(items):
    fresh = [i for i in items if i.expiry_days >= 0]
    fresh.sort(key = lambda i: (not i.is_almost_empty, i.expiry_days, i.name))
    return [i.name for i in fresh]