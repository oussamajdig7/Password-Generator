
import secrets
import string


def generate_password(length=16, uppercase=True,
                      lowercase=True, digits=True,
                      symbols=True):

    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*()-_=+"

    if not characters:
        raise ValueError("Select at least one character type.")

    if length < 1:
        raise ValueError("Password length must be positive.")

    password = []

    # Ensure at least one character from each selected type
    groups = []

    if uppercase:
        groups.append(string.ascii_uppercase)

    if lowercase:
        groups.append(string.ascii_lowercase)

    if digits:
        groups.append(string.digits)

    if symbols:
        groups.append("!@#$%^&*()-_=+")

    if length < len(groups):
        raise ValueError("Length is too short for selected options.")

    for group in groups:
        password.append(secrets.choice(group))

    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
