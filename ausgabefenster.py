# Import der benutzten Pakete
import json
from tkinter import *
import subprocess
import os


# Funktion die das Ausgabefenster schließt und zur Suche zurückkehrt
def back_button_action():
    ausgabefenster.destroy()
    if os.path.isfile("searchassist.json"):
        os.remove("searchassist.json")
    start_path = "./suchen.py"
    subprocess.run(["python", start_path])


# Funktion die das Ausgabefenster schließt und die Bearbeiten-maske öffnet
def change_button_action():
    pfad = "searchassist.json"
    if os.path.isfile(pfad):
        ausgabefenster.destroy()
        start_path = "./changeingfenster.py"
        subprocess.run(["python", start_path])
    else:
        message_label.config(
            text="Kunde wurde \ngelöscht!")


def delete_button_action():
    # Prüfen, ob die Datei existiert und löschen der entsprechenden ID
    if os.path.isfile("Kundendaten.json"):
        with open("Kundendaten.json", "r", encoding="utf-8") as file:
            kunden_daten = [json.loads(line) for line in file]

        # Filtern mit der ausgewählten ID
        kunden_daten = [kunde for kunde in kunden_daten if kunde.get("id")
                        != ausgabedaten["id"]]

        # Schreiben der aktualisierten Daten
        with open("Kundendaten.json", "w", encoding="utf-8") as file:
            for kunde in kunden_daten:
                json.dump(kunde, file, ensure_ascii=False)
                file.write("\n")

        message_label.config(text=f"{ausgabedaten['vorname']} "
                                  f"\n{ausgabedaten['nachname']} "
                                  f"\nwurde gelöscht.")
        os.remove("searchassist.json")


# Auslagerungsdatei öffnen und den zuvor gesuchten Kunden Laden
with open("searchassist.json", "r", encoding="utf-8") as reader:
    ausgabedaten = json.load(reader)
# Initialisieren des Ausgabefensters
ausgabefenster = Tk()
ausgabefenster.geometry("400x340")
ausgabefenster.title("Kunden Ausgabe")
# Erzeugen von Labels, Buttons und Eingabefeldern und deren Platzierung
kunden_vorname_label = Label(ausgabefenster, text="Vorname : ", anchor="w",
                             justify=LEFT)
kunden_vorname_label.place(x=20, y=20, width=360, height=20)
kunden_vorname_ausgabe_label = Label(ausgabefenster,
                                     text=ausgabedaten["vorname"], anchor="w",
                                     justify=LEFT)
kunden_vorname_ausgabe_label.place(x=140, y=20, width=360, height=20)

kunden_nachname_label = Label(ausgabefenster, text="Nachname : ", anchor="w",
                              justify=LEFT)
kunden_nachname_label.place(x=20, y=60, width=100, height=20)
kunden_nachname_ausgabe_label = Label(ausgabefenster,
                                      text=ausgabedaten["nachname"],
                                      anchor="w", justify=LEFT)
kunden_nachname_ausgabe_label.place(x=140, y=60, width=360, height=20)

kunden_geburtsdatum_label = Label(ausgabefenster, text="Geburtsdatum : ",
                                  anchor="w", justify=LEFT)
kunden_geburtsdatum_label.place(x=20, y=100, width=100, height=20)
kunden_geburtsdatum_ausgabe_label = Label(ausgabefenster,
                                          text=ausgabedaten["geburtsdatum"],
                                          anchor="w", justify=LEFT)
kunden_geburtsdatum_ausgabe_label.place(x=140, y=100, width=360, height=20)

kunden_mail_label = Label(ausgabefenster, text="E-Mail : ", anchor="w",
                          justify=LEFT)
kunden_mail_label.place(x=20, y=140, width=100, height=20)
kunden_mail_ausgabe_label = Label(ausgabefenster, text=ausgabedaten["email"],
                                  anchor="w", justify=LEFT)
kunden_mail_ausgabe_label.place(x=140, y=140, width=360, height=20)

kunden_ort_label = Label(ausgabefenster, text="Wohnort : ", anchor="w",
                         justify=LEFT)
kunden_ort_label.place(x=20, y=180, width=100, height=20)
kunden_ort_ausgabe_label = Label(ausgabefenster, text=ausgabedaten["wohnort"],
                                 anchor="w", justify=LEFT)
kunden_ort_ausgabe_label.place(x=140, y=180, width=360, height=20)

kunden_id_label = Label(ausgabefenster, text="Kundennummer : ", anchor="w",
                        justify=LEFT)
kunden_id_label.place(x=20, y=220, width=100, height=20)
kunden_id_ausgabe_label = Label(ausgabefenster, text=ausgabedaten["id"],
                                anchor="w", justify=LEFT)
kunden_id_ausgabe_label.place(x=140, y=220, width=360, height=20)

back_button = Button(ausgabefenster, text="<-Zurück",
                     command=back_button_action)
back_button.place(x=30, y=260, width=70, height=20)

change_button = Button(ausgabefenster, text="Bearbeiten",
                       command=change_button_action)
change_button.place(x=130, y=260, width=100, height=20)

exit_button = Button(ausgabefenster, text="Beenden",
                     command=ausgabefenster.quit)
exit_button.place(x=260, y=260, width=100, height=20)

message_label = Label(ausgabefenster, text=" ", anchor="w", justify=LEFT)
message_label.place(x=260, y=280, width=100, height=60)
delete_button = Button(ausgabefenster, text="Eintrag löschen",
                       command=delete_button_action, bg="red", fg="white")
delete_button.place(x=130, y=300, width=100, height=20)
# Funktion die auf Eingabe des Benutzers wartet
ausgabefenster.mainloop()
