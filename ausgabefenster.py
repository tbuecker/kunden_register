import json
from tkinter import *
import subprocess
import os

def back_button_action():
    ausgabefenster.destroy()
    #os.remove("searchassist.json")
    start_path = "./suchen.py"
    subprocess.run(["python", start_path])

def change_button_action():
    ausgabefenster.destroy()
    start_path = "changeingfenster.py"
    subprocess.run(["python", start_path])




with open("searchassist.json", "r", encoding="utf-8") as reader:
    ausgabedaten = json.load(reader)


ausgabefenster = Tk()
ausgabefenster.geometry("400x360")
ausgabefenster.title("Kunden Ausgabe")

kunden_vornme_label = Label(ausgabefenster,text="Vorname : ", anchor="w", justify=LEFT)
kunden_vornme_label.place(x=20, y=20, width= 360 , height= 20)
kunden_vornme_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["vorname"], anchor="w", justify=LEFT)
kunden_vornme_ausgabe_label.place(x=140, y=20, width= 360 , height= 20)

kunden_nachname_label = Label(ausgabefenster,text="Nachname : ", anchor="w", justify=LEFT)
kunden_nachname_label.place(x=20, y=60, width= 100 , height= 20)
kunden_nachname_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["nachname"], anchor="w", justify=LEFT)
kunden_nachname_ausgabe_label.place(x=140, y=60, width= 360 , height= 20)

kunden_geburtsdatum_label = Label(ausgabefenster,text="Geburtsdatum : ", anchor="w", justify=LEFT)
kunden_geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
kunden_geburtsdatum_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["geburtsdatum"], anchor="w", justify=LEFT)
kunden_geburtsdatum_ausgabe_label.place(x=140, y=100, width= 360 , height= 20)

kunden_mail_label = Label(ausgabefenster,text="E-Mail : ", anchor="w", justify=LEFT)
kunden_mail_label.place(x=20, y=140, width= 100 , height= 20)
kunden_mail_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["email"], anchor="w", justify=LEFT)
kunden_mail_ausgabe_label.place(x=140, y=140, width= 360 , height= 20)

kunden_ort_label = Label(ausgabefenster,text="Wohnort : ", anchor="w", justify=LEFT)
kunden_ort_label.place(x=20, y=180, width= 100 , height= 20)
kunden_ort_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["wohnort"], anchor="w", justify=LEFT)
kunden_ort_ausgabe_label.place(x=140, y=180, width= 360 , height= 20)

kunden_id_label = Label(ausgabefenster,text="Kundennummer : ", anchor="w", justify=LEFT)
kunden_id_label.place(x=20, y=220, width= 100 , height= 20)
kunden_id_ausgabe_label = Label(ausgabefenster,text=ausgabedaten["id"], anchor="w", justify=LEFT)
kunden_id_ausgabe_label.place(x=140, y=220, width= 360 , height= 20)

back_button = Button(ausgabefenster,text="<-Zurück", command=back_button_action)
back_button.place(x=30, y=260, width= 70 , height= 20)

change_button = Button(ausgabefenster,text="Bearbeiten", command=change_button_action)
change_button.place(x=130, y=260, width= 140 , height= 20)

ausgabefenster.mainloop()