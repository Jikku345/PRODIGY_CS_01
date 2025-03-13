import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# GUI Functions
def handle_encrypt():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        encrypted_text = encrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be a number!")

def handle_decrypt():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
        decrypted_text = decrypt(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be a number!")

# Create Main Window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")
root.configure(bg="#f4f4f4")

# Input Frame
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack(pady=10)

# Text Label and Input
label_text = tk.Label(frame, text="Enter Text:", bg="#f4f4f4", font=("Arial", 12))
label_text.grid(row=0, column=0, padx=5, pady=5)
entry_text = tk.Text(frame, height=3, width=40, font=("Arial", 12))
entry_text.grid(row=0, column=1, padx=5, pady=5)

# Shift Label and Input
label_shift = tk.Label(frame, text="Shift:", bg="#f4f4f4", font=("Arial", 12))
label_shift.grid(row=1, column=0, padx=5, pady=5)
entry_shift = tk.Entry(frame, font=("Arial", 12), width=5)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

# Buttons for Encrypt and Decrypt
button_encrypt = tk.Button(frame, text="Encrypt", command=handle_encrypt, font=("Arial", 12), bg="#4CAF50", fg="white", width=10)
button_encrypt.grid(row=2, column=0, padx=5, pady=5)

button_decrypt = tk.Button(frame, text="Decrypt", command=handle_decrypt, font=("Arial", 12), bg="#f44336", fg="white", width=10)
button_decrypt.grid(row=2, column=1, padx=5, pady=5)

# Output Label and Textbox
label_output = tk.Label(root, text="Output:", bg="#f4f4f4", font=("Arial", 12))
label_output.pack(pady=5)
output_text = tk.Text(root, height=3, width=40, font=("Arial", 12), bg="#e0e0e0", state="normal")
output_text.pack(pady=5)

# Run the Application
root.mainloop()
