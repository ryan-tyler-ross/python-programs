"""Practice loops by building and shuffling a password."""

import secrets
import string

password = []
for characters in (string.ascii_letters, string.digits, "!#$%&()*+"):
    for _ in range(9):
        password.append(secrets.choice(characters))

secrets.SystemRandom().shuffle(password)
print("Your new password:", "".join(password))
