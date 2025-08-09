import tkinter as tk
from tkinter import messagebox

# XOR encryption/decryption function
def xor_encrypt_decrypt(message, key):
    result = ""
    for i in range(len(message)):
        result += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return result

# Encrypt function
def encrypt():
    message = entry.get()
    key = key_entry.get()
    if not message or not key:
        messagebox.showwarning("Warning", "Please enter both message and key.")
        return
    encrypted = xor_encrypt_decrypt(message, key)
    # Show in hexadecimal for readability
    result_var.set(encrypted.encode().hex())

# Decrypt function
def decrypt():
    encrypted_hex = entry.get()
    key = key_entry.get()
    if not encrypted_hex or not key:
        messagebox.showwarning("Warning", "Please enter both encrypted text and key.")
        return
    try:
        encrypted = bytes.fromhex(encrypted_hex).decode()
        decrypted = xor_encrypt_decrypt(encrypted, key)
        result_var.set(decrypted)
    except Exception:
        messagebox.showerror("Error", "Invalid encrypted input.")

# Create GUI window
window = tk.Tk()
window.title("Key-based Encrypt / Decrypt")
window.geometry("400x300")
window.configure(bg="#1e1e2f")

# Title
tk.Label(window, text="Key-based Encrypt and Decrypt", fg="white", bg="#1e1e2f",font=("Book Antiqua", 20)).pack(pady=20)

# Message entry
tk.Label(window, text="Enter Message or Encrypted Text", fg="white", bg="#1e1e2f",font=("Arial",15)).pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(pady=9)

# Key entry
tk.Label(window, text="Enter Key", fg="white", bg="#1e1e2f",font=("Arial",15)).pack()
key_entry = tk.Entry(window, width=50)
key_entry.pack(pady=5)

# Buttons
frame = tk.Frame(window,bg="#1e1e2f")
frame.pack(pady=12)
tk.Button(frame, text="Encrypt", fg="white", bg="#06664e", font=("Arial", 15,"bold"), width=20, command=encrypt).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Decrypt",  fg="white", bg="#06664e", font=("Arial", 15,"bold"),width=20, command=decrypt).grid(row=0, column=1, padx=10)

# Result display
tk.Label(window, text="Result",fg="white", bg="#1e1e2f",font=("Arial",15)).pack()
result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, width=40, state="readonly").pack(pady=5)

# Run the app
window.mainloop()
