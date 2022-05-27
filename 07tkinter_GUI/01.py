import tkinter as tk

root = tk.Tk()
root.title('App Title')
root.geometry('350x400')
root.resizable(False,False)
print(root.winfo_width())
print(root.winfo_height())

root.mainloop()
