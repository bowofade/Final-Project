# Program name: OWOFADE_BABATUNDE_FINAL_PROJECT
# Author: Babatunde Owofade
# Date: 04/28/2022
# Summary: Domino's Pizza Ordering System
# Variables:

#   from pizzapy import Customer, StoreLocator, Address, 

#   customer = Customer("Babatunde", "Owofade", "bowofade@ivytech.edu", "3176409301", "6429 Mission Terrace, Indianaplis, IN, 46254")
 
#   my_local_dominos = StoreLocator.find_closest_store_to_customer(ccustomer)
print("my_local_dominos")
print("\nMENU\n")

#   menu = my_local_dominos.get_menu()
def searchMenu(menu):
    print("You are now searching the menu...")
    while True:
        item = input("Type an item to look for: ").strip().lower()

        if item != "" and len(item) > 1:
            item = item[0].upper() + item[1:]
        else:
            print("Invalid, exiting search...")
            break

        print(f"Resilts for: {item}")
        menu.search(Name=item)

searchMenu('menu')
