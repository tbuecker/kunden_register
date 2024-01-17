import json
import os
from tkinter import *
import subprocess

class Kunde:
    def __init__(self,vorname,nachname,geburtsdatum,email,wohnort):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum
        self.email = email
        self.wohnort = wohnort


def anlegen_button_action():

    kunde = Kunde(vorname_eingabe.get(), nachname_eingabe.get(), geburtsdatum_eingabe.get(), mail_eingabe.get(), ort_eingabe.get())
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json","a") as appender:
            json.dump(kunde.__dict__,appender)
    else:
        with open("Kundendaten.json", "w") as writer:
            json.dump(kunde.__dict__, writer)

#hier prüffunktionen#
#                   #
#####################


    message_label.config(text="Ein neuer Kunde wurde hinzugefügt")

    vorname_eingabe.delete(0,END)
    nachname_eingabe.delete(0, END)
    geburtsdatum_eingabe.delete(0, END)
    mail_eingabe.delete(0, END)
    ort_eingabe.delete(0, END)

def back_button_action():
    eingabefenster.destroy()
    start_path = "./startfenster.py"
    subprocess.run(["python", start_path])


eingabefenster = Tk()
eingabefenster.geometry("500x300")
eingabefenster.title("Kunden Eingabe")

vorname_label = Label(eingabefenster,text="Vorname : ")
vorname_label.place(x=20, y=20, width= 100 , height= 20)
vorname_eingabe=Entry(eingabefenster, bd=2)
vorname_eingabe.place(x=100, y=20, width=380, height= 20 )

nachname_label = Label(eingabefenster,text="Nachname : ")
nachname_label.place(x=20, y=60, width= 100 , height= 20)
nachname_eingabe=Entry(eingabefenster, bd=2)
nachname_eingabe.place(x=120, y=60, width=380, height= 20 )

geburtsdatum_label = Label(eingabefenster,text="Geburtsdatum : ")
geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
geburtsdatum_eingabe=Entry(eingabefenster, bd=2)
geburtsdatum_eingabe.place(x=100, y=100, width=380, height= 20 )

mail_label = Label(eingabefenster,text="E-Mail : ")
mail_label.place(x=20, y=140, width= 100 , height= 20)
mail_eingabe=Entry(eingabefenster, bd=2)
mail_eingabe.place(x=100, y=140, width=380, height= 20 )

ort_label = Label(eingabefenster,text="Wohnort : ")
ort_label.place(x=20, y=180, width= 100 , height= 20)
ort_eingabe=Entry(eingabefenster, bd=2)
ort_eingabe.place(x=100, y=180, width=380, height= 20 )

anlegen_button = Button(eingabefenster, text=" Als neuen Kunden anlegen ", command = anlegen_button_action)
anlegen_button.place(x=100,y=220,width=380,height=20)

message_label = Label(eingabefenster,text="")
message_label.place(x=100,y=260,width=380,height=20)

back_button = Button(eingabefenster,text="<-Zurück", command=back_button_action)
back_button.place(x=20, y=220, width= 70 , height= 20)

eingabefenster.mainloop()