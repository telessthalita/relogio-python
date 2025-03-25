from tkinter import *
import time
from datetime import datetime


formato_24h = True
modo_escuro = True

def toggle_format():
    global formato_24h
    formato_24h = not formato_24h
    update_time()

def toggle_theme():
    global modo_escuro
    modo_escuro = not modo_escuro
    if modo_escuro:
        root.configure(bg="#1a1a2e")
        time_label.configure(bg="#1a1a2e", fg="#e94560")
        date_label.configure(bg="#1a1a2e", fg="#e94560")
    else:
        root.configure(bg="#f5f5f5")
        time_label.configure(bg="#f5f5f5", fg="#222831")
        date_label.configure(bg="#f5f5f5", fg="#222831")

def update_time():
    now = datetime.now()
    if formato_24h:
        current_time = now.strftime("%H:%M:%S")
    else:
        current_time = now.strftime("%I:%M:%S %p")
    
    current_date = now.strftime("%A, %d %B %Y")  
    
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    time_label.after(1000, update_time)


root = Tk()
root.title("Relógio Digital Estilizado")
root.geometry("500x300")
root.configure(bg="#1a1a2e")


time_label = Label(root, font=("Helvetica", 50, "bold"), bg="#1a1a2e", fg="#e94560")
time_label.pack(pady=10)

date_label = Label(root, font=("Helvetica", 20, "italic"), bg="#1a1a2e", fg="#e94560")
date_label.pack()


button_style = {'font': ("Helvetica", 12), 'bg': "#0f3460", 'fg': "white", 'relief': "flat", 'padx': 20, 'pady': 10, 'bd': 2, 'highlightthickness': 0, 'activebackground': "#1a1a2e", 'activeforeground': "#e94560"}

toggle_time_btn = Button(root, text="Alternar Formato 12h/24h", command=toggle_format, **button_style)
toggle_time_btn.pack(pady=5)

toggle_theme_btn = Button(root, text="Alternar Modo Claro/Escuro", command=toggle_theme, **button_style)
toggle_theme_btn.pack(pady=5)

update_time()

root.mainloop()
