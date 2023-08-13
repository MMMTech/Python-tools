import tkinter as tk


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = self.winfo_screenwidth()
        self.height = self.winfo_screenheight()
        self.title("App")
        self.full_screen = f"{self.width}x{self.height}"
        self.windows = f"{self.width // 2}x{self.height // 2}"
        self.geometry(self.full_screen)
        print("App created!")


        btn = tk.Button(self, text="New Message", command=self.message)
        btn.pack()

        btn2 = tk.Button(self, text="Settings", command=self.settings)
        btn2.pack()

        sp = tk.Button(self, text="special window", command=self.special)
        sp.pack()


    def message(self):
        win = tk.Toplevel()
        win.title("Message")
        win.geometry(self.windows)
        label = tk.Label(win, text="Message Window")
        label.pack()
        win.grab_set()

    def settings(self):
        win = tk.Toplevel()
        win.title("Settings")
        win.geometry(self.windows)
        label = tk.Label(win, text="Settings Window")
        label.pack()
        win.grab_set()

    def special(self):
        sp = SpecialWindow()
        sp.title("Special")
        sp.geometry(self.windows)
        label = tk.Label(sp, text="Special Window")
        label.pack()
        sp.grab_set()

class SpecialWindow(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Special created!")

app = App()

app.mainloop()
