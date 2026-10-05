"""Generate a password with equal numbers of letters, digits, and symbols."""

import secrets
import string

def generate_password(per_group=9):
    password = []
    for characters in (string.ascii_letters, string.digits, "!#$%&()*+"):
        for _ in range(per_group):
            password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print("Your new password:", generate_password())


if __name__ == "__main__":
    main()
