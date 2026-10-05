# Password manager

Study Tkinter callbacks, encrypted file storage, and an in-memory dictionary.

From the course root: `python 06-desktop/password-manager/password_manager.py`.

Requires cryptography and pyperclip. The app creates data.enc beside the script and prompts for a master password. It derives a key with PBKDF2 and encrypts with Fernet; three wrong attempts close the app. Failed saves restore the previous in-memory entry. Keep the vault and master password available if you want to reopen saved entries.

- `password_manager.py` — Create or unlock an encrypted vault; add, search, generate, and view entries.
- `logo.png` — Image displayed at the top of the app.
- `.gitignore` — Exclude local vault files, environments, and editor settings.
