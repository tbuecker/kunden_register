import json
import os
from tkinter import *

class Kunde:
    def __init__(self,vorname,nachname,geburtsdatum,email,wohnort):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.email = email
        self.wohnort = wohnort

def button_action():
    kunde = Kunde(vorname.get(), nachname.get(), gebDatum.get(), mail.get(), ort.get())
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json","a") as appender:
            json.dump(kunde.__dict__,appender)
    else:
        with open("Kundendaten.json", "w") as writer:
            json.dump(kunde.__dict__, writer)
    message_label.config(text="Ein neuer Kunde wurde hinzugefügt")
    vorname.delete(0,END)
    nachname.delete(0, END)
    gebDatum.delete(0, END)
    mail.delete(0, END)
    ort.delete(0, END)


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