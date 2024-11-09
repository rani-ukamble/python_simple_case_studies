

def show_menus(menus):
    print(f"{'Code':<10} {'Item Name':<15} {'Price':<10} {'Stock':<10}")
    # 'Stock':<10==>
    # The string 'Stock' will be printed, left-aligned, and it will take up at least 10 characters of space.
    print("-" * 45)

    for item in menus:
        stock = "True" if item['stock'] else "No"
        print(f"{item['code']:<10} {item['itemname']:<15} {item['price']:<10} {stock:<10}")


def MakeOrder(menus, ordersList):
    sr_no = len(ordersList)

    order = input("Enter your order (e.g., M801 2,M802 1): ").split(',')
    curr_order = {'orderno':sr_no, 'menus':[]}
   
    for i in order:
        menucode , q = i.split() 
        q = int(q)
    
    

        menu = None # no dictionary is present
        for m in menus:
            if m['code'] == menucode:
                menu = m # here, menu is a single dictionary having particular menucode
                break
        
        if menu and menu['stock']:
            print(f"Menu '{menucode}' created order successfully")
        else:
            print(f"Menu '{menucode}' not exist. try again")

        curr_order['menus'].append({
                    'code': menucode,
                    'itemname': menu['itemname'],
                    'price': menu['price'],
                    'stock': True,
                    'quantity': q
                })

    ch = input("Please confirm your order: 'y' for yes and 'n' for no., 'd' for delete order and 'm' for modify [y/n/m/d]: ")
    if ch == 'y':
        ordersList.append(curr_order)
        print(f"Order no.- {sr_no} confirmed successfully!\n")
    elif ch == 'm':
        MakeOrder(menus, ordersList)
        
    elif ch == 'n':
        print("Order canceled.")
    elif ch =='d':
        del curr_order



def ShowOrderDetails(ordersList):
    for i in ordersList:
        print(f"#Order number : {i['orderno']}") 

        print(f"{'Code':<10} {'Item Name':<15} {'Price':<10} {'Qty':<10} {'Total':<10}")
        print("-" * 57)

        total = 0
        for item in i['menus']:
            cost = item['price'] * item['quantity']
            total+=cost

            print(f"{item['code']:<10} {item['itemname']:<15} {item['price']:<10} {item['quantity']:<10} {cost:<10}")

        print("-" * 55)
        print(f"Total {' '*42} {total}")
        print()

    
def show_inventory(ordersList):
    inventory = {}

    # Go through each order and summarize the inventory
    for order in ordersList:
        for menu in order['menus']:
            if menu['itemname'] in inventory:
                inventory[menu['itemname']]['issued_qty'] += menu['quantity']
                inventory[menu['itemname']]['amount'] += menu['price'] * menu['quantity']
            else:
                inventory[menu['itemname']] = {
                    'issued_qty': menu['quantity'],
                    'amount': menu['price'] * menu['quantity']
                }

    print(f"{'Menu Name':<17} {'IssuedQtys':<15} {'Amount':<10}")
    print("-" * 50)

    total_profit = 0
    for item, details in inventory.items():
        print(f"{item:<17} {details['issued_qty']:<15} {details['amount']:<10}")
        total_profit += details['amount']

    print("-" * 50)
    print(f"Total Profit{' ' * 25}{total_profit}")
