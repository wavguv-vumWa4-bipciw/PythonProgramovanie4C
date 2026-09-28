import tkinter as tk
from tkinter import messagebox

#---- Hlavne okno
hlavne_okno = tk.Tk()
hlavne_okno.title("Prve graficke okno vo Windows")
hlavne_okno.geometry("500x500")
hlavne_okno.resizable(False,False)
#----obsluha udalosti
def koniec():
    if messagebox.askyesno("Koniec", "Chceš ukončiť program ?"):
        hlavne_okno.destroy()

def pozdrav():
    messagebox.showinfo("Ahoj", "Pozdrav z programu")
#----Horne menu
menu = tk.Menu(hlavne_okno)
hlavne_okno.config(menu=menu)
menu_program = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Súbor", menu=menu_program)
menu_program.add_command(label="Nový",command="novy")
menu_program.add_command(label="Otvoriť",command="otvorit")
menu_program.add_command(label="Uložiť",command="ulozit")
menu_program.add_command(label="Uložiť ako ...",command="ulozit_ako")
menu_program.add_command(label="Koniec",command="koniec")

menu_info = tk.Menu(menu,tearoff=0)
menu.add_cascade(label="Info",menu=menu_info)
menu_info.add_command(label="O programe",
                      command=lambda: messagebox.showinfo("O programe",
                                                          "Vytvorene 4C"))

#telo hlavneho okna
tk.Label(hlavne_okno, text="Ako sa voláš ?", font=("Arial",12)).pack(pady=(15,5))
vstup_meno = tk.Entry(hlavne_okno, width=30,font=("Arial",11))
vstup_meno.pack()

#radio buton
tk.Label(hlavne_okno,text="Vyber si obľúbenú farbu",font=("Arial",12)).pack(pady=(15,5))
premenna_farba = tk.StringVar(value="Modrá")
ramec_farby = tk.Frame(hlavne_okno)
ramec_farby.pack()
for farba in ["Modrá", "Zelená", "červená"]:
    tk.Radiobutton(ramec_farby, text=farba,
                   variable=premenna_farba, value=farba).pack(side="left",padx=5)

#CheckButton
checkbox_var = tk.BooleanVar()
tk.Checkbutton(hlavne_okno,text="Mám rád Python",variable=checkbox_var).pack(pady=5)
checkbox_var_C = tk.BooleanVar()
tk.Checkbutton(hlavne_okno,text="Mám rád C++",variable=checkbox_var_C).pack(pady=5)

#Posuvnik (Scale)
tk.Label(hlavne_okno,text="Úroveň nálady od 1..10",font=("Arial",12)).pack()
posuvnik = tk.Scale(hlavne_okno,from_=1, to=10,orient="horizontal",length=250)
posuvnik.set(5)
posuvnik.pack(pady=5)

#Listbox
tk.Label(hlavne_okno,text="Vyber si obľúbený predmet:",font=("Arial",12)).pack()
zoznam = tk.Listbox(hlavne_okno,height=4,selectmode="single")
for predmet in ["Informatika","Matematika","Fyzika","Anglický jazyk", "Telesná"]:
    zoznam.insert(tk.END,predmet)
zoznam.pack()
#tlacidla
ramec_tlacidiel = tk.Frame(hlavne_okno)
ramec_tlacidiel.pack()

tk.Button(ramec_tlacidiel,text="Pozdrav", command=pozdrav,
          bg="black", fg="white", width=10).grid(row=0,column=0,padx=5)
tk.Button(ramec_tlacidiel,text="Koniec", command=koniec,
          bg="black", fg="white", width=10).grid(row=0,column=1,padx=5)

#zobrazenie okna - spustenie hlavneho cyklu
hlavne_okno.mainloop()

