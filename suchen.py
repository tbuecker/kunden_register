from tkinter import *
import subprocess


def back_button_action():
    suchfenster.destroy()
    start_path = "./startfenster.py"
    subprocess.run(["python", start_path])

def suchen_button_action():
    pass

suchfenster = Tk()
suchfenster.geometry("500x260")
suchfenster.title("Kunden Suche")

kunden_vornme_label = Label(suchfenster,text="Vorname : ")
kunden_vornme_label.place(x=20, y=20, width= 100 , height= 20)
kunden_vornme_eingabe=Entry(suchfenster, bd=2)
kunden_vornme_eingabe.place(x=120, y=20, width=360, height= 20 )

kunden_nachname_label = Label(suchfenster,text="Nachname : ")
kunden_nachname_label.place(x=20, y=60, width= 100 , height= 20)
kunden_nachname_eingabe=Entry(suchfenster, bd=2)
kunden_nachname_eingabe.place(x=120, y=60, width=360, height= 20 )

kunden_geburtsdatum_label = Label(suchfenster,text="Geburtsdatum : ")
kunden_geburtsdatum_label.place(x=20, y=100, width= 100 , height= 20)
kunden_geburtsdatum_eingabe=Entry(suchfenster, bd=2)
kunden_geburtsdatum_eingabe.place(x=120, y=100, width=360, height= 20 )

kunden_mail_label = Label(suchfenster,text="E-Mail : ")
kunden_mail_label.place(x=20, y=140, width= 100 , height= 20)
kunden_mail_eingabe=Entry(suchfenster, bd=2)
kunden_mail_eingabe.place(x=120, y=140, width=360, height= 20 )

kunden_ort_label = Label(suchfenster,text="Wohnort : ")
kunden_ort_label.place(x=20, y=180, width= 100 , height= 20)
kunden_ort_eingabe=Entry(suchfenster, bd=2)
kunden_ort_eingabe.place(x=120, y=180, width=360, height= 20 )

suchen_button = Button(suchfenster, text=" - Suchen - ", command=suchen_button_action)
suchen_button.place(x=120,y=220,width=360,height=20)

back_button = Button(suchfenster,text="<-Zurück", command=back_button_action)
back_button.place(x=30, y=220, width= 70 , height= 20)

suchfenster.mainloop()