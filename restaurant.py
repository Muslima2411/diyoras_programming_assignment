class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Reservation:
    def __init__(self, reservation_id, customer_name, selected_items, payment_method, status="Active"):
        self.reservation_id = reservation_id
        self.customer_name = customer_name
        self.selected_items = selected_items
        self.payment_method = payment_method
        self.status = status


class ReservationSystem:
    def __init__(self):
        self.menu = [
            MenuItem("Spaghetti Bolognese", 10.99),
            MenuItem("Caesar Salad", 8.99),
            MenuItem("Grilled Salmon", 12.99),
            MenuItem("Tiramisu", 15.99)
        ]
        self.reservations = []

    def find_reservation(self, reservation_id):
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                return reservation
        return None

    def view_menu(self):
        print("Menu:")
        for item in self.menu:
            print(f"{item.name}: ${item.price}")

    def calculate_total_price(self, selected_items):
        return sum(item.price for item in self.menu if item.name in selected_items)

    def print_reservation_details(self, reservation):
        print(f"Reservation ID: {reservation.reservation_id}")
        print(f"Customer: {reservation.customer_name}")
        print("Selected Items:")
        for item_name in reservation.selected_items:
            print(f"- {item_name}")
        print(f"Total Price: ${self.calculate_total_price(reservation.selected_items)}")
        print(f"Payment Method: {reservation.payment_method}")
        print(f"Status: {reservation.status}")
        print()

    def view_reservations(self, customer_name=None):
        filtered_reservations = self.reservations
        if customer_name:
            filtered_reservations = [r for r in filtered_reservations if r.customer_name == customer_name]

        if filtered_reservations:
            print("Reservations:")
            for reservation in filtered_reservations:
                self.print_reservation_details(reservation)
        else:
            print("No reservations found.")

    def add_reservation(self, customer_name, selected_items, payment_method):
        total_price = self.calculate_total_price(selected_items)
        if len(selected_items) > 10:
            print(f"Error: You can only select up to 10 items.")
            return

        reservation_id = len(self.reservations) + 1
        reservation = Reservation(reservation_id, customer_name, selected_items, payment_method, "Active")
        self.reservations.append(reservation)
        print(f"Reservation added successfully. Total Price: ${total_price}")

    def cancel_reservation(self, reservation_id):
        reservation = self.find_reservation(reservation_id)
        if reservation:
            reservation.status = 'Canceled'
            print(f"Reservation {reservation_id} canceled successfully.")
        else:
            print(f"Reservation with ID {reservation_id} not found.")


class CustomerReservationSystem(ReservationSystem):
    def view_reservation_details(self, reservation_id):
        reservation = self.find_reservation(reservation_id)
        if reservation:
            self.print_reservation_details(reservation)
        else:
            print(f"Reservation with ID {reservation_id} not found.")

    def update_customer_reservation(self, reservation_id, new_items):
        reservation = self.find_reservation(reservation_id)
        if reservation:
            reservation.selected_items = new_items
            reservation.status = "Modified"
            print(f"Reservation {reservation_id} updated successfully.")
        else:
            print(f"Reservation with ID {reservation_id} not found.")


class StaffReservationSystem(ReservationSystem):
    def view_payment_details(self, customer_name=None):
        filtered_reservations = self.reservations
        if customer_name:
            filtered_reservations = [r for r in filtered_reservations if r.customer_name == customer_name]

        if filtered_reservations:
            print("Payment Details:")
            for reservation in filtered_reservations:
                self.print_reservation_details(reservation)
        else:
            print("No reservations found.")

    def add_menu_item(self, new_item):
        self.menu.append(new_item)
        print(f"New menu item added: {new_item.name}")

    def update_menu_item(self, item_name, new_price):
        item = next((menu_item for menu_item in self.menu if menu_item.name == item_name), None)
        if item:
            item.price = new_price
            print(f"Menu item {item_name} updated successfully.")
        else:
            print(f"Menu item {item_name} not found.")

    def delete_menu_item(self, item_name):
        item = next((menu_item for menu_item in self.menu if menu_item.name == item_name), None)
        if item:
            self.menu.remove(item)
            print(f"Menu item {item_name} deleted successfully.")
        else:
            print(f"Menu item {item_name} not found.")


# Пример использования
customer_system = CustomerReservationSystem()
customer_system.view_menu()
customer_system.add_reservation("Alice Wonderland", ["Caesar Salad", "Tiramisu", "Grilled Salmon", "Spaghetti Bolognese", "Tiramisu"], "Cash")
customer_system.view_reservations("Alice Wonderland")
customer_system.update_customer_reservation(1, ["Spaghetti Bolognese", "Grilled Salmon", "Tiramisu"])
customer_system.view_reservation_details(1)
customer_system.add_reservation("Bob Builder", ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10", "Item11"], "Credit Card")
customer_system.cancel_reservation(1)
customer_system.view_reservations("Alice Wonderland")

staff_system = StaffReservationSystem()
staff_system.view_menu()
staff_system.add_menu_item(MenuItem("Shrimp Scampi", 18.99))
staff_system.update_menu_item("Spaghetti Bolognese", 11.99)
staff_system.view_menu()
staff_system.delete_menu_item("Grilled Salmon")
staff_system.view_menu()
staff_system.view_payment_details("Alice Wonderland")
