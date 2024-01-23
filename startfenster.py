# Import der benutzten Pakete
from tkinter import *
import subprocess


# Funktion die das Eingabefenster für neue Kunden öffnet
def anlegen_button_action():
    startfenster.destroy()
    anlegen_path = "eingabefenster.py"
    subprocess.run(["python", anlegen_path])


# Funktion die das Suchen-fenster öffnet
def suchen_button_action():
    startfenster.destroy()
    suchen_path = "./suchen.py"
    subprocess.run(["python", suchen_path])


# Initialisieren des Fensters
startfenster = Tk()
startfenster.title("Kunden-Verwaltung")
startfenster.geometry("500x100")
# Erstellen und Platzieren von Labels und Buttons
neuen_kunden_anlegen = Label(startfenster, text="Kunden anlegen : ")
neuen_kunden_anlegen.place(x=20, y=20, width=100, height=20)
neuen_kunden_anlegen_button = Button(startfenster, text="Neu",
                                     command=anlegen_button_action)
neuen_kunden_anlegen_button.place(x=140, y=20, width=100, height=20)

bestehenden_kunden_suchen = Label(startfenster, text="Kunden suchen : ")
bestehenden_kunden_suchen.place(x=260, y=20, width=100, height=20)
bestehenden_kunden_suchen_button = Button(startfenster, text="Suchen",
                                          command=suchen_button_action)
bestehenden_kunden_suchen_button.place(x=380, y=20, width=100, height=20)

beenden = Label(startfenster, text="Beenden : ")
beenden.place(x=20, y=60, width=100, height=20)
beenden_button = Button(startfenster, text="Beenden",
                        command=startfenster.quit)
beenden_button.place(x=140, y=60, width=340, height=20)

# Funktion die auf Eingabe des Benutzers wartet
startfenster.mainloop()
