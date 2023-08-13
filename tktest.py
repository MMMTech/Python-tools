import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Test Application")
root.config(background="white", padx=10, pady=10)
#root.geometry("600x600")

style = ttk.Style()
style.theme_use("clam")

img = tk.PhotoImage(file="python-logo.png")
img = img.subsample(2,2)

label = ttk.Label(root, text="Label", image=img, compound="left", background="white", padding=10, font=("Arial", 20))
label.pack(side="left")

entry = ttk.Entry(root, text="Default text", width=50, font=("Arial", 20))
entry.pack(side="left")

button = ttk.Button(root, text="Click")
button.pack(side="left")


root.mainloop()

