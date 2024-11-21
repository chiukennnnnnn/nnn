# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:30:13 2024

@author: user
"""

import tkinter as tk
from PIL import Image,ImageTk

def update_count():
    global click_count
    click_count=click_count+1
    count_label.config(text=f"點擊次數: {click_count}")

def on_click(event):
    c_label.config(image=o_m_i)
    window.after(200,lambda:c_label.config(image=c_m_i))
    update_count()
    
def resat_count():
    global click_count
    click_count=0
    count_label.config(text="點擊次數:0")



click_count=0

window=tk.Tk()
window.title("popcat,點擊遊戲")
window.geometry("400x500")
window.resizable(False,False)

c_m_i=ImageTk.PhotoImage(Image.open("8.png").resize((300,300)))
o_m_i=ImageTk.PhotoImage(Image.open("3.png").resize((300,300)))

c_label=tk.Label(window, image=c_m_i)
c_label.pack(pady=20)


count_label=tk.Label(window, text="點擊次數:0",font=("Arial",18))
count_label.pack(pady=10)


c_label.bind("<Button-1>",on_click)

resat_button=tk.Button(window,text="重置",command=resat_count,font=("Arial",14),bg="yellow")
resat_button.pack(pady=10)

window.mainloop()