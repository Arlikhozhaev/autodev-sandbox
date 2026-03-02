def calculate_discount(user, cart, promo_code):
    discount = _compute_discount(user, promo_code, cart)
    return cart.get("total", 0) * (1 - discount)


def _compute_discount(user, promo_code, cart):
    if not user:
        return 0

    if not user.get("is_premium"):
        if promo_code == "NEWUSER":
            return 0.10
        return 0

    if cart.get("total") <= 100:
        if promo_code:
            return 0.10
        return 0.05

    if promo_code != "SAVE20":
        return 0.15

    if user.get("account_age") > 365:
        return 0.30

    return 0.20
