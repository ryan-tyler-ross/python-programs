# Password manager example

[password_manager.py](password_manager.py) is a Tkinter app with password generation,
entry search, a vault listing, and master-password changes. It derives a key with
PBKDF2 and encrypts the local file with Fernet.

Entry: `python3 desktop/password-manager/password_manager.py`.
Dependencies: [cryptography and pyperclip](requirements.txt), plus a graphical desktop with Tk support.
[logo.png](logo.png) is the bundled UI asset.

The app creates `data.enc` beside the script and prompts to create or unlock it.
Three failed unlock attempts close the app. Local vault files are ignored by Git;
use sample entries when exploring the example.
