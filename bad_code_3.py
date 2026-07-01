def _is_valid_name(first_name, last_name):
    return bool(first_name and last_name)


def _is_valid_email(email):
    return bool(email and "@" in email)


def _is_valid_password(password):
    return bool(password and len(password) >= 8)


def _is_valid_phone(phone):
    return bool(phone)


def _is_valid_location(address, city, country):
    return bool(address and city and country)




def _validate_user_input(
    first_name, last_name, email, password,
    phone, address, city, country
):
    return all([
        first_name, last_name, email, password,
        phone, address, city, country
    ])


def create_user(
    first_name, last_name, email, password,
    phone, address, city, country, zip_code, role
):
    if not _validate_user_input(
        first_name, last_name, email, password,
        phone, address, city, country
    ):
        return None
    user = {
        "name": f"{first_name} {last_name}",
        "email": email,
        "phone": phone,
        "address": (
            f"{address}, {city},"
            f" {country} {zip_code}"
        ),
        "role": role or "user",
    }
    return user
