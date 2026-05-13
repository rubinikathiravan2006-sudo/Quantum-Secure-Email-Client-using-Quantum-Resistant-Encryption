import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
from cryptography.fernet import Fernet
import os

# ======================================
# GENERATE OR LOAD ENCRYPTION KEY
# ======================================
KEY_FILE = "secret.key"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)


if not os.path.exists(KEY_FILE):
    generate_key()

with open(KEY_FILE, "rb") as key_file:
    secret_key = key_file.read()

cipher = Fernet(secret_key)

# ======================================
# MAIN APPLICATION WINDOW
# ======================================
root = tk.Tk()
root.title("Quantum Secure Email Client")
root.geometry("900x650")
root.configure(bg="#0f172a")

# ======================================
# TITLE
# ======================================
title = tk.Label(
    root,
    text="Quantum Secure Email Client",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="cyan"
)

title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Cybersecurity-Based Secure Communication System",
    font=("Arial", 12),
    bg="#0f172a",
    fg="white"
)
subtitle.pack()

# ======================================
# USER DETAILS FRAME
# ======================================
frame = tk.Frame(root, bg="#1e293b", bd=2, relief=tk.RIDGE)
frame.pack(padx=20, pady=20, fill=tk.X)

# Sender Email
sender_label = tk.Label(frame, text="Sender Email", font=("Arial", 12, "bold"), bg="#1e293b", fg="white")
sender_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

sender_entry = tk.Entry(frame, width=50, font=("Arial", 11))
sender_entry.grid(row=0, column=1, padx=10, pady=10)

# Receiver Email
receiver_label = tk.Label(frame, text="Receiver Email", font=("Arial", 12, "bold"), bg="#1e293b", fg="white")
receiver_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

receiver_entry = tk.Entry(frame, width=50, font=("Arial", 11))
receiver_entry.grid(row=1, column=1, padx=10, pady=10)

# Subject
subject_label = tk.Label(frame, text="Subject", font=("Arial", 12, "bold"), bg="#1e293b", fg="white")
subject_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

subject_entry = tk.Entry(frame, width=50, font=("Arial", 11))
subject_entry.grid(row=2, column=1, padx=10, pady=10)

# ======================================
# MESSAGE BOX
# ======================================
message_label = tk.Label(
    root,
    text="Enter Secure Message",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="white"
)
message_label.pack()

message_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=12,
    font=("Arial", 11),
    bg="#f8fafc"
)
message_box.pack(padx=20, pady=10)

# ======================================
# ENCRYPT MESSAGE
# ======================================

def encrypt_message():
    message = message_box.get("1.0", tk.END).strip()

    if message == "":
        messagebox.showwarning("Warning", "Please enter a message")
        return

    encrypted_message = cipher.encrypt(message.encode())

    encrypted_box.delete("1.0", tk.END)
    encrypted_box.insert(tk.END, encrypted_message.decode())

    messagebox.showinfo("Success", "Message Encrypted Successfully")

# ======================================
# DECRYPT MESSAGE
# ======================================

def decrypt_message():
    encrypted_text = encrypted_box.get("1.0", tk.END).strip()

    if encrypted_text == "":
        messagebox.showwarning("Warning", "No encrypted message found")
        return

    try:
        decrypted_message = cipher.decrypt(encrypted_text.encode()).decode()

        decrypted_box.delete("1.0", tk.END)
        decrypted_box.insert(tk.END, decrypted_message)

        messagebox.showinfo("Success", "Message Decrypted Successfully")

    except:
        messagebox.showerror("Error", "Invalid Encryption Data")

# ======================================
# SAVE ENCRYPTED MESSAGE
# ======================================

def save_message():
    encrypted_text = encrypted_box.get("1.0", tk.END).strip()

    if encrypted_text == "":
        messagebox.showwarning("Warning", "No encrypted message to save")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(encrypted_text)

        messagebox.showinfo("Saved", "Encrypted message saved successfully")

# ======================================
# ENCRYPTED MESSAGE BOX
# ======================================
encrypted_label = tk.Label(
    root,
    text="Encrypted Message",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="cyan"
)
encrypted_label.pack()

encrypted_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=8,
    font=("Arial", 10),
    bg="#e2e8f0"
)
encrypted_box.pack(padx=20, pady=10)

# ======================================
# BUTTON FRAME
# ======================================
button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack(pady=15)

# Encrypt Button
encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt Message",
    font=("Arial", 12, "bold"),
    bg="#06b6d4",
    fg="white",
    padx=20,
    pady=10,
    command=encrypt_message
)

encrypt_btn.grid(row=0, column=0, padx=10)

# Decrypt Button
decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt Message",
    font=("Arial", 12, "bold"),
    bg="#10b981",
    fg="white",
    padx=20,
    pady=10,
    command=decrypt_message
)

decrypt_btn.grid(row=0, column=1, padx=10)

# Save Button
save_btn = tk.Button(
    button_frame,
    text="Save Secure File",
    font=("Arial", 12, "bold"),
    bg="#f59e0b",
    fg="white",
    padx=20,
    pady=10,
    command=save_message
)

save_btn.grid(row=0, column=2, padx=10)

# ======================================
# DECRYPTED MESSAGE BOX
# ======================================
decrypted_label = tk.Label(
    root,
    text="Decrypted Message",
    font=("Arial", 14, "bold"),
    bg="#0f172a",
    fg="lightgreen"
)
decrypted_label.pack()

decrypted_box = scrolledtext.ScrolledText(
    root,
    width=90,
    height=8,
    font=("Arial", 10),
    bg="#f8fafc"
)
decrypted_box.pack(padx=20, pady=10)

# ======================================
# FOOTER
# ======================================
footer = tk.Label(
    root,
    text="Future-Ready Cybersecurity Solution using Quantum-Resistant Encryption",
    font=("Arial", 10),
    bg="#0f172a",
    fg="white"
)
footer.pack(pady=10)

# ======================================
# START APPLICATION
# ======================================
root.mainloop()
