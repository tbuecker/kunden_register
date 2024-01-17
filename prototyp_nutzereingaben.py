import json
import os
from tkinter import *
import re

class Kunde:
    # Eine Klassenvariable für die ID-Zählung
    id_counter = 1

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
    pattern = r'^[a-zA-Z0-9ß][a-zA-Z0-9ß._-]*[a-zA-Z0-9ß]@[a-zA-Z0-9ß.-]+\.[a-zA-Z]{2,}$'
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

def button_action():
    email_input = mail.get()
    geburtsdatum_input = gebDatum.get()
    vorname_input = vorname.get()
    nachname_input = nachname.get()
    ort_input = ort.get()

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
        vorname.delete(0, END)
        nachname.delete(0, END)
        gebDatum.delete(0, END)
        mail.delete(0, END)
        ort.delete(0, END)
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
fenster = Tk()
# fenstertitle erstellen
fenster.title("Kunden Eingabe")

# infotext und button
erstellen = Button(fenster, text="Kunden hinzufügen", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)
vorname_label = Label(fenster, text="Vorname")
nachname_label = Label(fenster, text="Nachname")
gebdatum_label = Label(fenster, text="Geburtsdatum")
mail_label = Label(fenster,text = "MailAdresse")
ort_label = Label(fenster,text="Wohnort")
message_label = Label(fenster,text="")

vorname=Entry(fenster, bd=5, width=40)
nachname=Entry(fenster, bd=5, width=40)
gebDatum=Entry(fenster, bd=5, width=40)
mail=Entry(fenster, bd=5, width=40)
ort=Entry(fenster, bd=5, width=40)

# komponenten einfügen
vorname_label.pack()
vorname.pack()
nachname_label.pack()
nachname.pack()
gebdatum_label.pack()
gebDatum.pack()
mail_label.pack()
mail.pack()
ort_label.pack()
ort.pack()
message_label.pack()
erstellen.pack()
exit_button.pack()
#auf Eingabe des Benutzers warten.
fenster.mainloop()