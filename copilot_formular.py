import tkinter as tk
from tkinter import ttk, messagebox


def uloz_udaje():
    meno = meno_var.get()
    priezvisko = priezvisko_var.get()
    datum = datum_var.get()
    vek = vek_var.get()
    farba = farba_var.get()

    if not meno or not priezvisko:
        messagebox.showwarning("Chýbajú údaje", "Vyplňte meno a priezvisko.")
        return

    text = (
        f"MENO: {meno}\n"
        f"PRIEZVISKO: {priezvisko}\n"
        f"DÁTUM NARODENIA: {datum}\n"
        f"VEK: {vek}\n"
        f"OBĽÚBENÁ FARBA: {farba}"
    )

    vysledok.config(text=text)
    messagebox.showinfo("Úspech", "Údaje boli úspešne uložené.")


root = tk.Tk()
root.title("Evidencia používateľov")
root.geometry("650x550")
root.resizable(False, False)

BG = "#1e293b"
FRAME = "#334155"
BTN = "#3b82f6"
TEXT = "white"

root.configure(bg=BG)

nadpis = tk.Label(
    root,
    text="Evidencia používateľov",
    font=("Segoe UI", 22, "bold"),
    bg=BG,
    fg="#60a5fa"
)
nadpis.pack(pady=15)

frame = tk.Frame(root, bg=FRAME)
frame.pack(pady=10, padx=20, fill="both")

meno_var = tk.StringVar()
priezvisko_var = tk.StringVar()
datum_var = tk.StringVar()
vek_var = tk.StringVar()
farba_var = tk.StringVar()

style = ttk.Style()
style.theme_use("clam")

labels = ["Meno", "Priezvisko", "Dátum narodenia", "Vek", "Obľúbená farba"]
for i, txt in enumerate(labels):
    tk.Label(frame, text=txt, font=("Segoe UI", 11, "bold"), bg=FRAME, fg=TEXT).grid(row=i, column=0, padx=15, pady=10, sticky="w")

entry_meno = ttk.Entry(frame, textvariable=meno_var, width=35)
entry_meno.grid(row=0, column=1)

entry_priezvisko = ttk.Entry(frame, textvariable=priezvisko_var, width=35)
entry_priezvisko.grid(row=1, column=1)

entry_datum = ttk.Entry(frame, textvariable=datum_var, width=35)
entry_datum.grid(row=2, column=1)

spin_vek = ttk.Spinbox(frame, from_=1, to=120, textvariable=vek_var, width=33)
spin_vek.grid(row=3, column=1)

combo_farba = ttk.Combobox(
    frame,
    textvariable=farba_var,
    values=["Modrá", "Červená", "Zelená", "Žltá", "Fialová", "Čierna", "Biela"],
    state="readonly",
    width=32
)
combo_farba.grid(row=4, column=1)

btn = tk.Button(
    root,
    text="Uložiť údaje",
    font=("Segoe UI", 12, "bold"),
    bg=BTN,
    fg="white",
    border=0,
    command=uloz_udaje
)
btn.pack(pady=20)

vysledok = tk.Label(
    root,
    text="Tu sa zobrazia uložené údaje...",
    font=("Consolas", 11),
    bg="#0f172a",
    fg="#93c5fd",
    justify="left",
    width=55,
    height=10
)
vysledok.pack(pady=10)

root.mainloop()
