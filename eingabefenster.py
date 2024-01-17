import json
import os
from tkinter import *
import re
import subprocess

class Kunde:
    def __init__(self, vorname, nachname, geburtsdatum, email, wohnort):
        # Verwendung der ID-Zählung für jede Instanz
        self.id = Kunde.id_counter
        Kunde.id_counter += 1

        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.email = email
        self.wohnort = wohnort

def is_valid_email(email):
    # Verwendet eine einfache Regular Expression, um die Gültigkeit der E-Mail-Adresse zu überprüfen
    pattern = r'^[a-zA-Z0-9ß][a-zA-Z0-9ß._-]*@[a-zA-Z0-9ß.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_date(date):
    # Überprüft das Datumsformat "dd.mm.yyyy"
    date_pattern = r'^\d{2}\.\d{2}.\d{4}$'
    return re.match(date_pattern, date) is not None

def is_valid_name(name):
    # Überprüft, ob der Name nur Buchstaben enthält
    return name.isalpha()

def is_email_unique(email):
    # Überprüft, ob die eingegebene E-Mail schon vorhanden ist
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json", "r",  encoding="utf-8") as reader:
            for line in reader:
                kunden_daten = json.loads(line)
                if kunden_daten.get("email") == email:
                    return False
    return True

def get_last_id():
    # Funktion, um die zuletzt vergebene ID aus der Datei zu erhalten
    last_id = 0
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json", "r", encoding="utf-8") as file:
            for line in file:
                customer_data = json.loads(line)
                last_id = max(last_id, customer_data.get("id", 0))
    return last_id

def back_button_action():
    eingabefenster.destroy()
    start_path = "./startfenster.py"
    subprocess.run(["python", start_path])

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
        # Erhalte die zuletzt vergebene ID und setze die ID-Zählung fort
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
            message_label.config(text="Ungültige E-Mail-Adresse. Bitte erneut eingeben.")
        elif not is_valid_date(geburtsdatum_input):
            message_label.config(text="Ungültiges Geburtsdatum. Bitte im Format dd.mm.yyyy eingeben.")
        elif not is_valid_name(vorname_input):
            message_label.config(text="Ungültiger Vorname. Bitte nur Buchstaben verwenden.")
        elif not is_valid_name(nachname_input):
            message_label.config(text="Ungültiger Nachname. Bitte nur Buchstaben verwenden.")
        elif not is_valid_name(ort_input):
            message_label.config(text="Ungültiger Wohnort. Bitte nur Buchstaben verwenden.")
        elif not is_email_unique(email_input):
            message_label.config(text="Die E-Mail-Adresse wird bereits verwendet. Bitte eine andere verwenden.")






# fenster erstellen
eingabefenster = Tk()
eingabefenster.geometry("500x300")
eingabefenster.title("Kunden Eingabe")

vorname_label = Label(eingabefenster,text="Vorname : ", anchor="w", justify=LEFT)
vorname_label.place(x=20, y=20, width= 100 , height= 20)
vorname_eingabe=Entry(eingabefenster, bd=2)
vorname_eingabe.insert(0, "Falco")
vorname_eingabe.place(x=110, y=20, width=370, height= 20 )

nachname_label = Label(eingabefenster,text="Nachname : ", anchor="w", justify=LEFT)
nachname_label.place(x=20, y=60, width= 100 , height= 20)
nachname_eingabe=Entry(eingabefenster, bd=2)
nachname_eingabe.insert(0, "Kunath")
nachname_eingabe.place(x=110, y=60, width=370, height= 20 )

geburtsdatum_label = Label(eingabefenster,text="Geburtsdatum : ", anchor="w", justify=LEFT)
geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
geburtsdatum_eingabe=Entry(eingabefenster, bd=2)
geburtsdatum_eingabe.insert(0, "15.04.2017")
geburtsdatum_eingabe.place(x=110, y=100, width=370, height= 20 )

mail_label = Label(eingabefenster,text="E-Mail : ", anchor="w", justify=LEFT)
mail_label.place(x=20, y=140, width= 100 , height= 20)
mail_eingabe=Entry(eingabefenster, bd=2)
mail_eingabe.insert(0, "f.k@g.com")
mail_eingabe.place(x=110, y=140, width=370, height= 20 )

ort_label = Label(eingabefenster,text="Wohnort : ", anchor="w", justify=LEFT)
ort_label.place(x=20, y=180, width= 100 , height= 20)
ort_eingabe=Entry(eingabefenster, bd=2)
ort_eingabe.insert(0, "trebeltal")
ort_eingabe.place(x=110, y=180, width=370, height= 20 )

anlegen_button = Button(eingabefenster, text=" Als neuen Kunden anlegen ", command = anlegen_button_action)
anlegen_button.place(x=100,y=220,width=380,height=20)

message_label = Label(eingabefenster,text="")
message_label.place(x=110,y=260,width=370,height=20)

back_button = Button(eingabefenster,text="<-Zurück", command=back_button_action)
back_button.place(x=20, y=220, width= 70 , height= 20)

eingabefenster.mainloop()