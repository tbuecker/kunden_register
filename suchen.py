# Import der benutzten Pakete
from tkinter import *
import subprocess
import json


# Funktion die das Suchfenster schließt und zum Startfenster zurückkehrt
def back_button_action():
    suchfenster.destroy()
    start_path = "./startfenster.py"
    subprocess.run(["python", start_path])


# Funktion die eingegebene Daten in der Kundendatei sucht
def suchen_button_action():
    vorname_input = kunden_vorname_eingabe.get()
    nachname_input = kunden_nachname_eingabe.get()
    geburtsdatum_input = kunden_geburtsdatum_eingabe.get()
    mail_input = kunden_mail_eingabe.get()
    ort_input = kunden_ort_eingabe.get()
    id_input_str = kunden_id_eingabe.get()

    if not (vorname_input and nachname_input or id_input_str):
        message_label.config(
            text="Alle mit [*] markierten Felder ODER Kunden ID müssen "
                 "ausgefüllt werden!")
        return
    # Überprüfen, ob die Eingabe für die Kunden-ID nicht leer ist
    if id_input_str:
        id_input = int(id_input_str)
    else:
        # wenn die Eingabe leer ist, setze id_input auf None
        id_input = None

    # Initialize a list to store matched customer data
    matched_customers = []

    with open("Kundendaten.json", "r", encoding="utf-8") as file:
        for line in file:
            customer_data = json.loads(line)

            # Check if the entered search criteria match
            if (
                    (not vorname_input or customer_data.get(
                        "vorname") == vorname_input) and
                    (not nachname_input or customer_data.get(
                        "nachname") == nachname_input) and
                    (not geburtsdatum_input or customer_data.get(
                        "geburtsdatum") == geburtsdatum_input) and
                    (not mail_input or customer_data.get(
                        "email") == mail_input) and
                    (not ort_input or customer_data.get(
                        "wohnort") == ort_input) and
                    (id_input is None or customer_data.get(
                        "id") == id_input)
            ):
                matched_customers.append(customer_data)

    # Check the number of matches
    num_matches = len(matched_customers)

    if num_matches == 0:
        message_label.config(text="Kunde wurde nicht gefunden!")
    elif num_matches == 1:
        # Only one match found, proceed to display or process it
        with open("searchassist.json", "w", encoding="utf-8") as writer:
            json.dump(matched_customers[0], writer, ensure_ascii=False)
        suchfenster.destroy()
        ausgabe_path = "./ausgabefenster.py"
        subprocess.run(["python", ausgabe_path])
    else:
        # Multiple matches found, provide appropriate feedback
        message_label.config(
            text=f"{num_matches} Treffer gefunden. Präzisiere deine Suche.")


# Initialisieren des Suchfensters
suchfenster = Tk()
suchfenster.geometry("500x350")
suchfenster.title("Kunden Suche")
# Erzeugen von Labels, Buttons und Eingabefeldern und deren Platzierung
kunden_vorname_label = Label(suchfenster, text="Vorname : [*]", anchor="w",
                             justify=LEFT)
kunden_vorname_label.place(x=20, y=20, width=100, height=20)
kunden_vorname_eingabe = Entry(suchfenster, bd=2)
kunden_vorname_eingabe.place(x=120, y=20, width=360, height=20)

kunden_nachname_label = Label(suchfenster, text="Nachname : [*]", anchor="w",
                              justify=LEFT)
kunden_nachname_label.place(x=20, y=60, width=100, height=20)
kunden_nachname_eingabe = Entry(suchfenster, bd=2)
kunden_nachname_eingabe.place(x=120, y=60, width=360, height=20)

kunden_ort_label = Label(suchfenster, text="Wohnort : ", anchor="w",
                         justify=LEFT)
kunden_ort_label.place(x=20, y=100, width=100, height=20)
kunden_ort_eingabe = Entry(suchfenster, bd=2)
kunden_ort_eingabe.place(x=120, y=100, width=360, height=20)

kunden_mail_label = Label(suchfenster, text="E-Mail : ", anchor="w",
                          justify=LEFT)
kunden_mail_label.place(x=20, y=140, width=100, height=20)
kunden_mail_eingabe = Entry(suchfenster, bd=2)
kunden_mail_eingabe.place(x=120, y=140, width=360, height=20)

kunden_geburtsdatum_label = Label(suchfenster, text="Geburtsdatum : ",
                                  anchor="w", justify=LEFT)
kunden_geburtsdatum_label.place(x=20, y=180, width=100, height=20)
kunden_geburtsdatum_eingabe = Entry(suchfenster, bd=2)
kunden_geburtsdatum_eingabe.place(x=120, y=180, width=360, height=20)

kunden_id_label = Label(suchfenster, text="Kunden ID : ", anchor="w",
                        justify=LEFT)
kunden_id_label.place(x=20, y=220, width=100, height=20)
kunden_id_eingabe = Entry(suchfenster, bd=2)
kunden_id_eingabe.place(x=120, y=220, width=360, height=20)

suchen_button = Button(suchfenster, text=" - Suchen - ",
                       command=suchen_button_action)
suchen_button.place(x=120, y=260, width=360, height=20)

back_button = Button(suchfenster, text="<-Zurück", command=back_button_action)
back_button.place(x=30, y=260, width=70, height=20)

message_label = Label(suchfenster, text=" ", anchor="w", justify=LEFT)
message_label.place(x=150, y=280, width=300, height=40)

# Funktion die auf Eingabe des Benutzers wartet
suchfenster.mainloop()
