import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter - Frame a LabelFrame")
root.geometry("480x360")

#-----------
# Frame - obyčajný kontajner bez názvu
#----------
frame = tk.Frame(root, bg="#E3F2FD",padx=15,pady=15)
frame.pack(fill="x",padx=15,pady=15)

ttk.Label(frame,text="Toto je obyčajný Frame",background="#E3F2FD").pack()
ttk.Button(frame,text="Tlačidlo vo Frame").pack(pady=5)

#-------------------
# LabelFrame
#-------------------
label_frame = ttk.LabelFrame(root,text="Údaje u žiakoch",padding=15)
label_frame.pack(fill="x",padx=15,pady=15)

ttk.Label(label_frame,text="Meno a priezvisko :").grid(row=0,column=0,sticky="w",pady=5)
ttk.Entry(label_frame).grid(row=0,column=1,padx=10,pady=5)
ttk.Label(label_frame,text="Trieda :").grid(row=1,column=0,sticky="w",pady=5)
ttk.Entry(label_frame).grid(row=1,column=1,padx=10,pady=5)
ttk.Button(label_frame,text="Uložiť").grid(row=2,column=0,columnspan=2,sticky="w",pady=10)
#zobrazíme hlavné okno
root.mainloop()
