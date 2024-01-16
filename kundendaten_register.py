import json

class Customer:
    def __init__(self, name, age, email, locations=None, unique_id=None, additional_fields=None):
        self.name = name
        self.age = age
        self.email = email
        self.locations = locations or []
        self.unique_id = unique_id
        self.additional_fields = additional_fields or {}

class CustomerDatabase:
    def __init__(self, filename="customer_data.json"):
        self.filename = filename
        self.customers = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for customer_id, customer_data in data.items():
                    self.customers[int(customer_id)] = Customer(**customer_data)
        except FileNotFoundError:
            pass  # No existing data file

    def save_data(self):
        with open(self.filename, 'w') as file:
            data = {str(customer.unique_id): vars(customer) for customer in self.customers.values()}
            json.dump(data, file, indent=2)

    def add_customer(self, customer):
        if customer.unique_id is None:
            customer.unique_id = max(self.customers.keys(), default=0) + 1
        self.customers[customer.unique_id] = customer
        self.save_data()

    def update_customer(self, customer_id, new_data):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            for key, value in new_data.items():
                setattr(customer, key, value)
            self.save_data()
        else:
            print("Customer not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            self.save_data()
        else:
            print("Customer not found.")

    def display_customers(self):
        for customer_id, customer in self.customers.items():
            print(f"Customer ID: {customer_id}")
            print(f"Name: {customer.name}")
            print(f"Age: {customer.age}")
            print(f"Email: {customer.email}")
            print(f"Locations: {', '.join(customer.locations)}")
            print("Additional Fields:")
            for field, value in customer.additional_fields.items():
                print(f"  {field}: {value}")
            print()

if __name__ == "__main__":
    db = CustomerDatabase()

    while True:
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Display Customers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            age = input("Enter customer age: ")
            email = input("Enter customer email: ")
            locations = input("Enter customer locations (comma-separated): ").split(',')
            additional_fields = {}
            while True:
                field = input("Enter additional field name (or press Enter to finish): ")
                if not field:
                    break
                value = input(f"Enter value for {field}: ")
                additional_fields[field] = value

            new_customer = Customer(name, age, email, locations=locations, additional_fields=additional_fields)
            db.add_customer(new_customer)
            print("Customer added successfully.")

        elif choice == "2":
            customer_id = int(input("Enter customer ID to update: "))
            update_data = {}
            while True:
                field = input("Enter field to update (or press Enter to finish): ")
                if not field:
                    break
                value = input(f"Enter new value for {field}: ")
                update_data[field] = value
            db.update_customer(customer_id, update_data)
            print("Customer updated successfully.")

        elif choice == "3":
            customer_id = int(input("Enter customer ID to delete: "))
            db.delete_customer(customer_id)
            print("Customer deleted successfully.")

        elif choice == "4":
            db.display_customers()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
