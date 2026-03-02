def create_user(first_name, last_name, email, password, phone, address, city, country, zip_code, role):
    if not first_name or not last_name:
        return None
    if not email or "@" not in email:
        return None
    if not password or len(password) < 8:
        return None
    if not phone:
        return None
    if not address or not city or not country:
        return None
    user = {
        "name": f"{first_name} {last_name}",
        "email": email,
        "phone": phone,
        "address": f"{address}, {city}, {country} {zip_code}",
        "role": role or "user"
    }
    return user