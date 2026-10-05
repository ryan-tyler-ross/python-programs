import json
import os
import string
import sys
from base64 import urlsafe_b64encode
from secrets import choice, token_bytes
from tkinter import (
    Tk, Toplevel, Canvas, Label, Entry, Button, Frame, Listbox, Scrollbar,
    StringVar, PhotoImage, END, messagebox, simpledialog,
)

import pyperclip
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ---------------------------- CONSTANTS ------------------------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_FILE = os.path.join(BASE_DIR, "data.enc")
LOGO_FILE = os.path.join(BASE_DIR, "logo.png")

SYMBOLS = "!#$%&()*+"
PASSWORD_LENGTH = 16
SALT_BYTES = 16
KDF_ITERATIONS = 600_000  # OWASP 2023 recommendation for PBKDF2-HMAC-SHA256
MIN_MASTER_LENGTH = 8


# ---------------------------- CRYPTO ------------------------------- #
def derive_key(password, salt):
    """Stretch a master password into a Fernet-compatible 32-byte key."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=KDF_ITERATIONS,
    )
    return urlsafe_b64encode(kdf.derive(password.encode("utf-8")))


def load_vault(password):
    """Read and decrypt the vault. Returns (entries_dict, salt, key)."""
    with open(VAULT_FILE, "rb") as f:
        salt = f.read(SALT_BYTES)
        ciphertext = f.read()
    key = derive_key(password, salt)
    plaintext = Fernet(key).decrypt(ciphertext)  # raises InvalidToken on wrong password
    return json.loads(plaintext.decode("utf-8")), salt, key


def save_vault(entries_dict, salt, key):
    """Encrypt entries and atomically replace the vault file."""
    ciphertext = Fernet(key).encrypt(json.dumps(entries_dict).encode("utf-8"))
    tmp = VAULT_FILE + ".tmp"
    with open(tmp, "wb") as f:
        f.write(salt + ciphertext)
    os.replace(tmp, VAULT_FILE)


# ---------------------------- UNLOCK / CREATE ------------------------------- #
def unlock_or_create():
    """Prompt for master password to either create a fresh vault or open an existing one.
    Returns (entries_dict, salt, key); exits on cancel or repeated failure."""
    root = Tk()
    root.withdraw()

    if not os.path.exists(VAULT_FILE):
        while True:
            pw1 = simpledialog.askstring("Create vault", "Choose a master password:", show="*", parent=root)
            if pw1 is None:
                root.destroy(); sys.exit(0)
            if len(pw1) < MIN_MASTER_LENGTH:
                messagebox.showerror("Weak password", f"Must be at least {MIN_MASTER_LENGTH} characters.", parent=root)
                continue
            pw2 = simpledialog.askstring("Create vault", "Confirm master password:", show="*", parent=root)
            if pw2 is None:
                root.destroy(); sys.exit(0)
            if pw1 != pw2:
                messagebox.showerror("Mismatch", "Passwords didn't match. Try again.", parent=root)
                continue
            salt = token_bytes(SALT_BYTES)
            key = derive_key(pw1, salt)
            save_vault({}, salt, key)
            root.destroy()
            return {}, salt, key

    for remaining in range(3, 0, -1):
        pw = simpledialog.askstring("Unlock vault", "Master password:", show="*", parent=root)
        if pw is None:
            root.destroy(); sys.exit(0)
        try:
            result = load_vault(pw)
            root.destroy()
            return result
        except InvalidToken:
            if remaining > 1:
                messagebox.showerror("Wrong password", f"Incorrect. {remaining - 1} attempt(s) left.", parent=root)
    messagebox.showerror("Locked out", "Too many failed attempts.", parent=root)
    root.destroy(); sys.exit(1)


# ---------------------------- APP STATE ------------------------------- #
# Loaded when the application starts.


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    chars = string.ascii_letters + string.digits + SYMBOLS
    password = "".join(choice(chars) for _ in range(PASSWORD_LENGTH))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    try:
        pyperclip.copy(password)
    except pyperclip.PyperclipException:
        pass  # Clipboard unavailable; password is still visible in the entry box.


# ---------------------------- SAVE / ADD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showinfo("Oops", "Please don't leave any fields empty.")
        return

    if website in entries:
        if not messagebox.askokcancel("Overwrite?", f"An entry for '{website}' already exists. Overwrite it?"):
            return

    previous = entries.get(website)
    entries[website] = {"email": email, "password": password}
    try:
        save_vault(entries, salt, key)
    except OSError as e:
        if previous is None:
            del entries[website]
        else:
            entries[website] = previous
        messagebox.showerror("Save failed", str(e))
        return

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


# ---------------------------- ENTRY POPUP (shared by Search and View Vault) ------------------------------- #
def show_entry_popup(website, entry):
    """Display a stored entry's email and (masked) password in a small dialog."""
    popup = Toplevel(window)
    popup.title(website)
    popup.config(padx=20, pady=20)
    popup.transient(window)
    popup.resizable(False, False)

    Label(popup, text="Website:", anchor="e", width=10).grid(row=0, column=0, sticky="e", pady=2)
    Label(popup, text=website).grid(row=0, column=1, sticky="w", padx=(10, 0), pady=2)

    Label(popup, text="Email:", anchor="e", width=10).grid(row=1, column=0, sticky="e", pady=2)
    Label(popup, text=entry["email"]).grid(row=1, column=1, sticky="w", padx=(10, 0), pady=2)

    Label(popup, text="Password:", anchor="e", width=10).grid(row=2, column=0, sticky="e", pady=2)
    masked = "•" * len(entry["password"])
    pw_var = StringVar(value=masked)
    Label(popup, textvariable=pw_var, font=("Courier", 10)).grid(row=2, column=1, sticky="w", padx=(10, 0), pady=2)

    shown = [False]
    def toggle_show():
        shown[0] = not shown[0]
        pw_var.set(entry["password"] if shown[0] else masked)
        show_btn.config(text="Hide" if shown[0] else "Show")

    show_btn = Button(popup, text="Show", width=6, command=toggle_show)
    show_btn.grid(row=2, column=2, padx=(10, 0))

    def copy_pw():
        try:
            pyperclip.copy(entry["password"])
            copy_btn.config(text="Copied!")
            popup.after(1500, lambda: copy_btn.config(text="Copy password"))
        except pyperclip.PyperclipException:
            messagebox.showerror("Clipboard unavailable", "Couldn't copy to clipboard.", parent=popup)

    button_row = Frame(popup)
    button_row.grid(row=3, column=0, columnspan=3, pady=(15, 0), sticky="ew")
    copy_btn = Button(button_row, text="Copy password", width=15, command=copy_pw)
    copy_btn.pack(side="left", padx=(0, 5))
    Button(button_row, text="Close", width=10, command=popup.destroy).pack(side="right")

    popup.bind("<Escape>", lambda _e: popup.destroy())


# ---------------------------- SEARCH (Option A) ------------------------------- #
def search():
    website = website_entry.get().strip()
    if not website:
        messagebox.showinfo("Oops", "Type a website name to search for.")
        return
    entry = entries.get(website)
    if entry is None:
        messagebox.showinfo("Not found", f"No entry for '{website}'.")
        return
    show_entry_popup(website, entry)


# ---------------------------- VIEW VAULT (Option B) ------------------------------- #
def view_vault():
    """Open a window listing every saved website; double-click or 'View' to see details."""
    popup = Toplevel(window)
    popup.title("Vault")
    popup.config(padx=20, pady=20)
    popup.transient(window)

    if not entries:
        Label(popup, text="No entries saved yet.").pack()
        Button(popup, text="Close", command=popup.destroy).pack(pady=(15, 0))
        popup.bind("<Escape>", lambda _e: popup.destroy())
        return

    Label(popup, text=f"{len(entries)} saved site(s) — double-click to view").pack(anchor="w")

    list_frame = Frame(popup)
    list_frame.pack(fill="both", expand=True, pady=(10, 10))

    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(list_frame, yscrollcommand=scrollbar.set, width=40, height=12, activestyle="dotbox")
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=listbox.yview)

    sorted_sites = sorted(entries.keys(), key=str.lower)
    for site in sorted_sites:
        listbox.insert(END, site)

    def open_selected(_event=None):
        sel = listbox.curselection()
        if not sel:
            return
        site = sorted_sites[sel[0]]
        show_entry_popup(site, entries[site])

    listbox.bind("<Double-Button-1>", open_selected)
    listbox.bind("<Return>", open_selected)

    button_row = Frame(popup)
    button_row.pack(fill="x")
    Button(button_row, text="View selected", command=open_selected).pack(side="left")
    Button(button_row, text="Close", command=popup.destroy).pack(side="right")

    popup.bind("<Escape>", lambda _e: popup.destroy())


# ---------------------------- CHANGE MASTER PASSWORD ------------------------------- #
def change_master_password():
    global salt, key
    new1 = simpledialog.askstring("Change master password", "New master password:", show="*", parent=window)
    if new1 is None:
        return
    if len(new1) < MIN_MASTER_LENGTH:
        messagebox.showerror("Weak password", f"Must be at least {MIN_MASTER_LENGTH} characters.")
        return
    new2 = simpledialog.askstring("Change master password", "Confirm new master password:", show="*", parent=window)
    if new2 is None:
        return
    if new1 != new2:
        messagebox.showerror("Mismatch", "Passwords didn't match.")
        return
    new_salt = token_bytes(SALT_BYTES)
    new_key = derive_key(new1, new_salt)
    try:
        save_vault(entries, new_salt, new_key)
    except OSError as e:
        messagebox.showerror("Save failed", str(e))
        return
    salt, key = new_salt, new_key
    messagebox.showinfo("Done", "Master password changed.")


# ---------------------------- UI ------------------------------- #
entries, salt, key = unlock_or_create()
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file=LOGO_FILE)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
Button(text="Search Database", width=13, command=search).grid(row=1, column=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)
Button(text="Generate Password", command=generate_password).grid(row=3, column=2)

Button(text="Add", width=36, command=save).grid(row=4, column=1, columnspan=2, pady=(10, 0))
Button(text="View Vault", width=36, command=view_vault).grid(row=5, column=1, columnspan=2)
Button(text="Change Master Password", width=36, command=change_master_password).grid(row=6, column=1, columnspan=2)

window.mainloop()
