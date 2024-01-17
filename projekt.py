import json

# Datenbank erstellen
def create_database():
    data = []
    for i in range(3):
        name = input("Geben Sie den Namen des Kunden ein: ")
        age = input("Geben Sie das Alter des Kunden ein: ")
        email = input("Geben Sie die E-Mail-Adresse des Kunden ein: ")
        data.append({"name": name, "age": age, "email": email})
    with open("Kundendaten.json", "w") as f:
        json.dump(data, f)

# Datenbank durchsuchen
def search_database():
    with open("Kundendaten.json", "r") as f:
        data = json.load(f)
    name = input("Geben Sie den Namen des Kunden ein, nach dem Sie suchen möchten: ")
    for customer in data:
        if customer["name"] == name:
            print(f"Name: {customer['name']}")
            print(f"Alter: {customer['age']}")
            print(f"E-Mail-Adresse: {customer['email']}")
            break
    else:
        print(f"Der Kunde mit dem Namen {name} wurde nicht gefunden.")

# Datenbank erstellen
create_database()

# Datenbank durchsuchen
search_database()