

def show_menus(menus):
    # Set column widths
    code_width = 5
    name_width = 15
    price_width = 10
    stock_width = 10

    # Print header
    print(f"{'Code'.ljust(code_width)} {'Item Name'.ljust(name_width)} {'Price'.ljust(price_width)} {'Stock'.ljust(stock_width)}")
    print("-" * (code_width + name_width + price_width + stock_width))

    # Print items
    for i in menus:
        stock_status = "True" if i['stock'] else "False"
        print(f"{i['code'].ljust(code_width)} {i['itemname'].ljust(name_width)} {str(i['price']).ljust(price_width)} {stock_status.ljust(stock_width)}")


# def MakeOrder(menus, ordersList):
#     orderDict = {}

#     # Step 1: Get the order input from the user
#     order = input("Enter your order (e.g., M801 2,M802 1): ")
#     order = order.split(',')  # Split orders by comma

#     # Step 2: Parse the input and store it in orderDict
#     for i in order:
#         l = i.split()  # Split each entry by space
#         if len(l) == 2:
#             orderDict[l[0]] = int(l[1])  # l[0] is the menu code, l[1] is the quantity


#     # Step 3: Validate the input and check menu availability
#     for key, value in orderDict.items():  # Iterate over orderDict
#         menu_item = None  # Initialize menu_item to None for each key
#         for item in menus:  # Loop through each item in menus
#             if item['code'] == key:  # Check if the item's code matches the key
#                 menu_item = item  # Set menu_item to the found item

#                 break  



#         if menu_item is None:  # Menu item not found
#             print(f"Menu {key} does not exist. Please try again.")
#         elif not menu_item['stock']:  # Out of stock
#             print(f"{menu_item['itemname']} is out of stock.")
#         else:  # Valid order
#             ordersList.append({'code': key, 'itemname': menu_item['itemname'], 'quantity': value})
#             print(f"{value}  {menu_item['itemname']} ordered successfully.")
        
        
    


#     code_width = 5
#     stock_width = 5
#     price_width = 5
#     name_width = 15
#     quantity_width = 10

    
#     # 3 Order Confirmation
#     confirm = input("Enter 'y' for order confirmation else 'n' for not ")
#     if confirm == 'y':
#         # Print header
#         print(f"{'Code'.ljust(code_width)} {'Item Name'.ljust(name_width)} {'Quantity'.ljust(quantity_width)} {'Code'.ljust(code_width)} {'Price'.ljust(price_width)} {'Stock'.ljust(stock_width)}")
#         print("-" * (code_width + name_width + quantity_width + stock_width + price_width))

        


#         for order in ordersList:
#             print(f"{order['code'].ljust(code_width)} {order['itemname'].ljust(name_width)} {str(order['quantity']).ljust(quantity_width)} {str(order['price']).ljust(quantity_width)} {str(order['stock']).ljust(quantity_width)}")

#         for i in menus:
#             stock_status = "Yes" if i['stock'] else "No"
#             print(f"{i['code'].ljust(code_width)} {i['itemname'].ljust(name_width)} {str(i['price']).ljust(price_width)} {stock_status.ljust(stock_width)}")




def MakeOrder(menus, ordersList):
    orderDict = {}

    # Step 1: Get the order input from the user
    order = input("Enter your order (e.g., M801 2,M802 1): ")
    order = order.split(',')  # Split orders by comma

    # Step 2: Parse the input and store it in orderDict
    for i in order:
        l = i.split()  # Split each entry by space
        if len(l) == 2:
            orderDict[l[0]] = int(l[1])  # l[0] is the menu code, l[1] is the quantity

    # Step 3: Validate the input and check menu availability
    for key, value in orderDict.items():  # Iterate over orderDict
        menu_item = None  # Initialize menu_item to None for each key
        for item in menus:  # Loop through each item in menus
            if item['code'] == key:  # Check if the item's code matches the key
                menu_item = item  # Set menu_item to the found item
                break

        if menu_item is None:  # Menu item not found
            print(f"Menu {key} does not exist. Please try again.")
        elif not menu_item['stock']:  # Out of stock
            print(f"{menu_item['itemname']} is out of stock.")
        else:  # Valid order
            # Store price, stock, and other details from the menu
            # ordersList.append({
            #     'code': key,
            #     'itemname': menu_item['itemname'],
            #     'quantity': value,
            #     'price': menu_item['price'],
            #     'stock': menu_item['stock']
            # })
            ordersList.append({
                
                'itemname': menu_item['itemname'],
               
                'price': menu_item['price'],
                'stock': menu_item['stock']
            })
            print(f"{value} {menu_item['itemname']} ordered successfully.")

    # Step 4: Order confirmation
    confirm = input("Enter 'y' for order confirmation else 'n' for not: ")
    if confirm == 'y':
        # Set column widths for displaying order details
        code_width = 5
        name_width = 15
        quantity_width = 10
        price_width = 10
        stock_width = 10

        # Print header
        print(f"{'Code'.ljust(code_width)} {'Item Name'.ljust(name_width)} {'Quantity'.ljust(quantity_width)} {'Price'.ljust(price_width)} {'Stock'.ljust(stock_width)}")
        print("-" * (code_width + name_width + quantity_width + price_width + stock_width))

        # Display each order
        for order in ordersList:
            stock_status = "Yes" if order['stock'] else "No"
            print(f"{order['code'].ljust(code_width)} {order['itemname'].ljust(name_width)} {str(order['quantity']).ljust(quantity_width)} {str(order['price']).ljust(price_width)} {stock_status.ljust(stock_width)}")



def ShowOrderDetails(ordersList):
    # Set column widths
    code_width = 5
    name_width = 15
    quantity_width = 10

    # Print header
    print(f"{'Code'.ljust(code_width)} {'Item Name'.ljust(name_width)} {'Quantity'.ljust(quantity_width)}")
    print("-" * (code_width + name_width + quantity_width))

    for order in ordersList:
        print(f"{order['code'].ljust(code_width)} {order['itemname'].ljust(name_width)} {str(order['quantity']).ljust(quantity_width)}")


    
        
    