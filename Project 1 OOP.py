class Foods:
    def __init__(self, name, price): 
        self.name = name
        self.price = price

class Order:    # DITO PARA MAG ADD YUNG MGA ITEMS PARA SA MGA PAGKAIN
    def __init__(self): 
        self.items = []

    def add_item(self, item): 
        self.items.append(item) 
        print(f"Added {item.name} to your order.")

    def total(self):            #SUM PRICE
        return sum(item.price for item in self.items)
    
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return
        
        print("\nYour order:")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₱{item.price}")
        print(f"Total: ₱{self.total()}\n")

    def checkout(self):                        # FOR BUYING
        if not self.items:
            print("Your cart is empty.")
            return
        
        self.show_order()
        confirm = input("Magpatuloy sa pag-checkout? (oo/hindi): ").strip().lower()
        if confirm == 'oo':
            print("Nakumpirma na ang order! Salamat po.") 
            self.items.clear()
        else: 
            print("Pag-kansela ng pag-checkout.")

def main():
        # LIST NA AVAILABLE NA CUISINE
    menu_list = [
        Foods("Adobo", 75),
        Foods("Sinigang", 75),
        Foods("Lechon", 95),
        Foods("Kare-Kare", 75),
        Foods("Sisig", 95),
        Foods("Crispy Pata", 95),
    ]

    order = Order()

    while True:
        print("\n ╼╼╼╼╼╼╼╼╼ FILIPINO MENU ╼╼╼╼╼╼╼╼╼")
        for i, pagkain in enumerate(menu_list, 1):
            print(f"{i}. {pagkain.name} - ₱{pagkain.price}")

        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            index = int(choice) - 1
            order.add_item(menu_list[index])    
            
        elif choice == '7':
            order.checkout()
        elif choice == '8':
            print("Maraming salamat po!")
            break
        else:
            print("Invalid option. Kindly try again.")

if __name__ == "__main__":
    main()