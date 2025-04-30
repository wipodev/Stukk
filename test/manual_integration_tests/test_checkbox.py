import tkinter
import customtkinter

app = customtkinter.CTk()
app.title('Test Checkbox Focus Traversal')
app.geometry('400x500')

variables = [tkinter.BooleanVar(value=False) for _ in range(7)]

def make_callback(index):
    def callback():
        print(f"Checkbox {index + 1}: {variables[index].get()}")
    return callback

for i in range(7):
    customtkinter.CTkCheckBox(
        app,
        text=f"Option {i + 1}",
        variable=variables[i],
        command=make_callback(i)
    ).pack(pady=20, padx=10)


app.mainloop()
