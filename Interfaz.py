import tkinter as tk

app = tk.Tk()
app.geometry("300x600")
app.configure(background= "black")
tk.Wm.wm_title(app, "VENTA DE ACCESORIOS")

tk.Button(
        app,
        text="click",
        font=("courier", 15),
        bg="#10a4dfc5",
        fg="white"
    ).pack(
        fill= tk.BOTH,
        expand=True,
        
    )


app.mainloop()
