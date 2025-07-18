import tkinter as tk
from tkinter import messagebox
import os

folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "ContactosCRUD")
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, "friendsContact.txt")

root = tk.Tk()
root.title("Contactos CRUD")

tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Number").grid(row=1, column=0, padx=5, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=5, pady=5)

def create():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if not name or not number:
        messagebox.showwarning("Warning", "Name and Number cannot be empty.")
        return

    if not number.isdigit():
        messagebox.showerror("Error", "Number must contain only digits.")
        return

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(name + "!"):
                    messagebox.showinfo("Message", "Friend already exists.")
                    return

    with open(file_path, 'a') as file:
        file.write(f"{name}!{number}\n")
    messagebox.showinfo("Message", "Friend added.")

def read():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Warning", "Name cannot be empty.")
        return

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith(name + "!"):
                    number = line.strip().split("!")[1]
                    number_entry.delete(0, tk.END)
                    number_entry.insert(0, number)
                    messagebox.showinfo("Message", "Friend found.")
                    return
    messagebox.showinfo("Message", "Friend not found.")

def update():
    name = name_entry.get().strip()
    number = number_entry.get().strip()

    if not name or not number:
        messagebox.showwarning("Warning", "Name and Number cannot be empty.")
        return

    if not number.isdigit():
        messagebox.showerror("Error", "Number must contain only digits.")
        return

    updated = False
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.startswith(name + "!"):
                    file.write(f"{name}!{number}\n")
                    updated = True
                else:
                    file.write(line)
    if updated:
        messagebox.showinfo("Message", "Friend updated.")
    else:
        messagebox.showinfo("Message", "Friend not found.")

def delete():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning("Warning", "Name cannot be empty.")
        return

    deleted = False
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if not line.startswith(name + "!"):
                    file.write(line)
                else:
                    deleted = True
    if deleted:
        messagebox.showinfo("Message", "Friend deleted.")
    else:
        messagebox.showinfo("Message", "Friend not found.")

tk.Button(root, text="Create", width=10, command=create).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text="Read", width=10, command=read).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Update", width=10, command=update).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text="Delete", width=10, command=delete).grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
