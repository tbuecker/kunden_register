import json
import os
from tkinter import *
import re
from tkinter import messagebox

class Kunde:
    id_counter = 1

    def __init__(self, vorname, nachname, geburtsdatum, email, wohnort):
        self.id = Kunde.id_counter
        Kunde.id_counter += 1
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.email = email
        self.wohnort = wohnort

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9ß][a-zA-Z0-9ß._-]*@[a-zA-Z0-9ß.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_date(date):
    date_pattern = r'^\d{2}\.\d{2}.\d{4}$'
    return re.match(date_pattern, date) is not None

def is_valid_name(name):
    return name.isalpha()

def is_email_unique(email):
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json", "r",  encoding="utf-8") as reader:
            for line in reader:
                kunden_daten = json.loads(line)
                if kunden_daten.get("email") == email:
                    return False
    return True

def get_last_id():
    last_id = 0
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json", "r", encoding="utf-8") as file:
            for line in file:
                customer_data = json.loads(line)
                last_id = max(last_id, customer_data.get("id", 0))
    return last_id

def back_button_action():
    eingabefenster.destroy()
    messagebox.showinfo("Zurück", "Zurücktaste wurde gedrückt!")

def anlegen_button_action():
    email_input = mail_eingabe.get()
    geburtsdatum_input = geburtsdatum_eingabe.get()
    vorname_input = vorname_eingabe.get()
    nachname_input = nachname_eingabe.get()
    ort_input = ort_eingabe.get()

    if (
        is_valid_email(email_input) and
        is_valid_date(geburtsdatum_input) and
        is_valid_name(vorname_input) and
        is_valid_name(nachname_input) and
        is_valid_name(ort_input) and
        is_email_unique(email_input)
    ):
        last_id = get_last_id()
        Kunde.id_counter = last_id + 1

        kunde = Kunde(vorname_input, nachname_input, geburtsdatum_input, email_input, ort_input)
        with open("Kundendaten.json", "a",  encoding="utf-8") as appender:
            json.dump(kunde.__dict__, appender, ensure_ascii=False)
            appender.write("\n")
        message_label.config(text=f"Ein neuer Kunde mit der ID {kunde.id} wurde hinzugefügt")
        vorname_eingabe.delete(0, END)
        nachname_eingabe.delete(0, END)
        geburtsdatum_eingabe.delete(0, END)
        mail_eingabe.delete(0, END)
        ort_eingabe.delete(0, END)
    else:
        if not is_valid_email(email_input):
            messagebox.showwarning("Ungültige E-Mail-Adresse", "Ungültige E-Mail-Adresse. Bitte erneut eingeben.")
        elif not is_valid_date(geburtsdatum_input):
            messagebox.showwarning("Ungültiges Geburtsdatum", "Ungültiges Geburtsdatum. Bitte im Format dd.mm.yyyy eingeben.")
        elif not is_valid_name(vorname_input):
            messagebox.showwarning("Ungültiger Vorname", "Ungültiger Vorname. Bitte nur Buchstaben verwenden.")
        elif not is_valid_name(nachname_input):
            messagebox.showwarning("Ungültiger Nachname", "Ungültiger Nachname. Bitte nur Buchstaben verwenden.")
        elif not is_valid_name(ort_input):
            messagebox.showwarning("Ungültiger Wohnort", "Ungültiger Wohnort. Bitte nur Buchstaben verwenden.")
        elif not is_email_unique(email_input):
            messagebox.showwarning("Doppelte E-Mail-Adresse", "Die E-Mail-Adresse wird bereits verwendet. Bitte eine andere verwenden.")

# Fenster erstellen
eingabefenster = Tk()
eingabefenster.geometry("500x300")
eingabefenster.title("Kunden Eingabe")

# Entry-Felder und Labels erstellen
labels = ["Vorname", "Nachname", "Geburtsdatum", "E-Mail", "Wohnort"]
entries = []

for i, label_text in enumerate(labels):
    label = Label(eingabefenster, text=f"{label_text} : ")
    label.place(x=20, y=20 + 40 * i, width=100, height=20)
    entry = Entry(eingabefenster, bd=2)
    entry.place(x=120, y=20 + 40 * i, width=380, height=20)
    entries.append(entry)

# Anlegen-Button und zurück-Button erstellen
anlegen_button = Button(eingabefenster, text="Als neuen Kunden anlegen", command=anlegen_button_action)
anlegen_button.place(x=100, y=220, width=380, height=20)

message_label = Label(eingabefenster, text="")
message_label.place(x=100, y=260, width=380, height=20)

back_button = Button(eingabefenster, text="<- Zurück", command=back_button_action)
back_button.place(x=20, y=220, width=70, height=20)

eingabefenster.mainloop()
