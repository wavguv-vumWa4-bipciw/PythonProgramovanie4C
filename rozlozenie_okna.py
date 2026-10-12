import tkinter as tk
from struct import pack
from tkinter import ttk

root = tk.Tk()
root.title("Projekt - rozloženie okna")
root.geometry("520x420")
root.resizable(False,False)

#PACK - prvky sa radia nad seba alebo vedla seba
pack_frame = tk.LabelFrame(root,text="1 - radenie prvkov",padx=10,pady=10 )
pack_frame.pack(fill="x",padx=10, pady=10)

tk.Button(pack_frame,text="Hore", bg="#4CAf50", fg="white").pack(side="top",fill="x")
tk.Button(pack_frame,text="Vľavo", bg="#4CAa50", fg="white").pack(side="left",expand=True,
                                                                  fill="x",padx=5)
tk.Button(pack_frame,text="Vpravo", bg="#4CFf50", fg="white").pack(side="right",expand=True,
                                                                   fill="x",padx=5)
#Grid - prvky sú rozložené v riadkoch a stĺpcoch
grid_frame = tk.LabelFrame(root,text= "2 - rozloženie pomocou grid",padx=10,pady=10)
grid_frame.pack(fill = "x",padx=10,pady=10)
ttk.Label(grid_frame, text="Meno:").grid(row=0,column=0,sticky="w",padx= 5,pady=5)
ttk.Entry(grid_frame).grid(row=0,column=1,padx= 5,pady=5 )

ttk.Label(grid_frame, text="Priezvisko:").grid(row=1,column=0,sticky="w",padx= 5,pady=5)
ttk.Entry(grid_frame).grid(row=1,column=1,padx= 5,pady=5 )

ttk.Label(grid_frame, text="Trieda:").grid(row=2,column=0,sticky="w",padx= 5,pady=5)
ttk.Entry(grid_frame).grid(row=2,column=1,padx= 5,pady=5 )

ttk.Button(grid_frame,text="Uložiť").grid(row=3,column=0,columnspan=2,sticky="we",pady=5)
#Zobrazenie okna
root.mainloop()
