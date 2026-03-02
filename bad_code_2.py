def calculate_discount(user, cart, promo_code):
    discount = 0
    if user:
        if user.get("is_premium"):
            if cart.get("total") > 100:
                if promo_code == "SAVE20":
                    if user.get("account_age") > 365:
                        discount = 0.30
                    else:
                        discount = 0.20
                else:
                    discount = 0.15
            else:
                if promo_code:
                    discount = 0.10
                else:
                    discount = 0.05
        else:
            if promo_code == "NEWUSER":
                discount = 0.10
    return cart.get("total", 0) * (1 - discount)