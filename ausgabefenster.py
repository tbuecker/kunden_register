import json
from tkinter import *
import subprocess
import os

def back_button_action():
    ausgabefenster.destroy()
    os.remove("searchassist.json")
    start_path = "./suchen.py"
    subprocess.run(["python", start_path])

with open("searchassist.json", "r", encoding="utf-8") as reader:
    ausgabedaten = json.load(reader)


ausgabefenster = Tk()
ausgabefenster.geometry("500x260")
ausgabefenster.title("Kunden Ausgabe")

kunden_vornme_label = Label(ausgabefenster,text="Vorname")
kunden_vornme_label.place(x=20, y=20, width= 100 , height= 20,anchor="w")
kunden_vornme_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["vorname"])
kunden_vornme_ausgabe_label.place(x=140, y=20, width= 360 , height= 20)

kunden_nachname_label = Label(ausgabefenster,text="Nachname : ")
kunden_nachname_label.place(x=20, y=60, width= 100 , height= 20)
kunden_nachname_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["nachname"])
kunden_nachname_ausgabe_label.place(x=140, y=60, width= 360 , height= 20)

kunden_geburtsdatum_label = Label(ausgabefenster,text="Geburtsdatum : ")
kunden_geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
kunden_geburtsdatum_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["geburtsdatum"])
kunden_geburtsdatum_ausgabe_label.place(x=140, y=100, width= 360 , height= 20)

kunden_mail_label = Label(ausgabefenster,text="E-Mail : ")
kunden_mail_label.place(x=20, y=140, width= 100 , height= 20)
kunden_mail_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["email"])
kunden_mail_ausgabe_label.place(x=140, y=140, width= 360 , height= 20)

kunden_ort_label = Label(ausgabefenster,text="Wohnort : ")
kunden_ort_label.place(x=20, y=180, width= 100 , height= 20)
kunden_ort_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["wohnort"])
kunden_ort_ausgabe_label.place(x=140, y=180, width= 360 , height= 20)

back_button = Button(ausgabefenster,text="<-Zurück", command=back_button_action)
back_button.place(x=30, y=220, width= 70 , height= 20)

ausgabefenster.mainloop()