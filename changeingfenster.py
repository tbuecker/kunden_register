import json
from tkinter import *
import re
import subprocess
import os

class Kunde:
    id_counter = 1  # Initialisiere id_counter

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
    pattern = r'[a-zA-Z0-9ß]*[._-]?[a-zA-Z0-9ß]*[._-]?[a-zA-Z0-9ß]*@[a-zA-Z0-9ß]*[._-]?[a-zA-Z0-9ß]*[._-]?[a-zA-Z0-9ß]*\.[a-zA-Z0-9ß]{2,}'
    return re.match(pattern, email) is not None

def is_valid_date(date):
    # Überprüft das Datumsformat "dd.mm.yyyy"
    date_pattern = r'^\d{2}\.\d{2}.\d{4}$'
    return re.match(date_pattern, date) is not None

def is_valid_name(name):
    # Überprüft, ob der Name nur Buchstaben enthält
    return name.isalpha()

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
    changefenster.destroy()
    start_path = "./suchen.py"
    subprocess.run(["python", start_path])

def change_button_action():
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
        is_valid_name(ort_input)
    ):
        # Überprüfe, ob die Datei existiert und bearbeite den Datensatz mit der entsprechenden ID
        if os.path.isfile("Kundendaten.json"):
            with open("Kundendaten.json", "r", encoding="utf-8") as file:
                kunden_daten = [json.loads(line) for line in file]

                for kunde in kunden_daten:
                    if kunde.get("id") == ausgabedaten["id"]:
                        kunde["vorname"] = vorname_input
                        kunde["nachname"] = nachname_input
                        kunde["geburtsdatum"] = geburtsdatum_input
                        kunde["email"] = email_input
                        kunde["wohnort"] = ort_input

            with open("Kundendaten.json", "w", encoding="utf-8") as file:
                # Schreibe jedes JSON-Objekt in eine separate Zeile
                for kunde in kunden_daten:
                    json.dump(kunde, file, ensure_ascii=False)
                    file.write("\n")

        message_label.config(text=f"{ausgabedaten['vorname']} {ausgabedaten['nachname']} wurde geändert.")
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

# Hier holt der Code die Kundendaten aus der searchassist.json-Datei
with open("searchassist.json", "r", encoding="utf-8") as reader:
    ausgabedaten = json.load(reader)

# fenster erstellen
changefenster = Tk()
changefenster.geometry("500x340")
changefenster.title("Kunden Bearbeitung")

vorname_label = Label(changefenster,text="Vorname : ", anchor="w", justify=LEFT)
vorname_label.place(x=20, y=20, width= 100 , height= 20)
vorname_eingabe=Entry(changefenster, bd=2)
vorname_eingabe.insert(0, ausgabedaten["vorname"])
vorname_eingabe.place(x=110, y=20, width=370, height= 20 )

nachname_label = Label(changefenster,text="Nachname : ", anchor="w", justify=LEFT)
nachname_label.place(x=20, y=60, width= 100 , height= 20)
nachname_eingabe=Entry(changefenster, bd=2)
nachname_eingabe.insert(0, ausgabedaten["nachname"])
nachname_eingabe.place(x=110, y=60, width=370, height= 20 )

geburtsdatum_label = Label(changefenster,text="Geburtsdatum : ", anchor="w", justify=LEFT)
geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
geburtsdatum_eingabe=Entry(changefenster, bd=2)
geburtsdatum_eingabe.insert(0, ausgabedaten["geburtsdatum"])
geburtsdatum_eingabe.place(x=110, y=100, width=370, height= 20 )

mail_label = Label(changefenster,text="E-Mail : ", anchor="w", justify=LEFT)
mail_label.place(x=20, y=140, width= 100 , height= 20)
mail_eingabe=Entry(changefenster, bd=2)
mail_eingabe.insert(0, ausgabedaten["email"])
mail_eingabe.place(x=110, y=140, width=370, height= 20 )

ort_label = Label(changefenster,text="Wohnort : ", anchor="w", justify=LEFT)
ort_label.place(x=20, y=180, width= 100 , height= 20)
ort_eingabe=Entry(changefenster, bd=2)
ort_eingabe.insert(0, ausgabedaten["wohnort"])
ort_eingabe.place(x=110, y=180, width=370, height= 20 )

id_label = Label(changefenster,text="Kundenummer : ", anchor="w", justify=LEFT)
id_label.place(x=20, y=220, width= 100 , height= 20)
id_label_ausgabe = Label(changefenster,text=ausgabedaten["id"],anchor="w", justify=LEFT)
id_label_ausgabe.place(x=140,y=220,width=370,height=20)

message_label = Label(changefenster,text="")
message_label.place(x=50,y=300,width=400,height=20)

back_button = Button(changefenster,text="<-Zurück", command=back_button_action)
back_button.place(x=20, y=260, width= 70 , height= 20)
change_button = Button(changefenster,text="Bearbeitung Speichern", command=change_button_action)
change_button.place(x=130, y=260, width= 140 , height= 20)

changefenster.mainloop()