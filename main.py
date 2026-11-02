
from password_generator import generate_password

print("=" * 40)
print("       SECURE PASSWORD GENERATOR")
print("=" * 40)

try:
    length = int(input("Password length: "))
    count = int(input("Number of passwords: "))

    uppercase = input("Include uppercase? (y/n): ").lower() == "y"
    lowercase = input("Include lowercase? (y/n): ").lower() == "y"
    digits = input("Include numbers? (y/n): ").lower() == "y"
    symbols = input("Include symbols? (y/n): ").lower() == "y"

    print("\nGenerated Passwords:")
    print("-" * 40)

    for i in range(count):
        password = generate_password(
            length,
            uppercase,
            lowercase,
            digits,
            symbols
        )

        print(f"{i + 1}. {password}")

except ValueError as error:
    print("Error:", error)
