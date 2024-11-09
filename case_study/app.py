

from operation1 import show_menus, MakeOrder, ShowOrderDetails, ShowOrderDetails, show_inventory

menus = [
    {'code': 'M801', 'itemname': 'sandwich', 'price': 190, 'stock': True},
    {'code': 'M802', 'itemname': 'pizza', 'price': 150, 'stock': False},
    {'code': 'M803', 'itemname': 'burger', 'price': 160, 'stock': True},
    {'code': 'M804', 'itemname': 'colddrink', 'price': 50, 'stock': True},
    {'code': 'M805', 'itemname': 'coffee', 'price': 70, 'stock': True},
    {'code': 'M806', 'itemname': 'roll', 'price': 150, 'stock': True}
]

ordersList = list()

while True:
    print()
    print("[1]. Show Menu List: ")
    print("[2]. Make Order ")
    print("[3]. Show Orders List : ")
    print("[4]. Inventories ")
    print("[5]. Exit ")

    choice = int(input("Select Menu: "))
    print()
    
    if choice == 1:
        show_menus(menus)
    elif choice == 2:
        MakeOrder(menus, ordersList)
    elif choice == 3:
        ShowOrderDetails(ordersList)
    elif choice == 4:
        show_inventory(ordersList)
    elif choice == 5:
        break
    else:
        print("Invalid menu. Try again.")
