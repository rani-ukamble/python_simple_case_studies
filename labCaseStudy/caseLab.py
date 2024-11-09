

def showMenus(menus):
    if type(menus) == list:
        for item in menus:
            print("%20s %20s %10d %10s"%(item['code'],item['itemname'],item['price'],item['stock']))


# def makeOrder(menus, ordersList):

#     sr_no = len(ordersList)

#     curr_order = {'orderno':sr_no, 'menus':[]}

#     customerOrder = input("Describe your order <menucode> <qty> :")
#     #"M801 3, M804 2, M701 5"

#     if type(menus) == list:
#         codeList = [item['code'] for item in menus]
#         co = [item.split(" ") for item in customerOrder.split(",")]
#         #['M801 3', 'M804 2','M701 5'] -> [['M801','3'], ['M804', '2'],['M701', '5']]

#         tempOrderList = list()
#         for orderItem in co:
#             d = dict()
#             d['code'] = orderItem[0]
#             d['qty'] = int(orderItem[1])

#             if d['code'] in codeList:
#                 d['status'] = 'valid'
#                 print('Menu ',d['code'],'created order successfully')
#             else:
#                 d['status'] = 'invalid'
#                 print('Menu ',d['code'],'not exist. try again')
            
#             curr_order['menus'].append(dict)

#             # tempOrderList.append(d)
        

#         print(tempOrderList)
#         ch = input("do you want to process this order [y/n]? :")
#         if ch == 'y':
#             return tempOrderList
#         elif ch == 'n':
#             ch1 = input('modify/cancel order [m/c] ?')
#             if ch1== 'm':
#                 for eachItem in tempOrderList:
#                     print("%20s %10d %10s"%(eachItem['code'],eachItem['qty'],eachItem['status']))

#                     qty = int(input("Enter new Qtys :"))
#                     eachItem['qty'] = qty
#                     if eachItem['qty']==0:
#                         tempOrderList.remove(eachItem)
            
#             elif ch1=='c':
#                 print("Your order is canceled ")
#                 print("Thanks! have a great day.")
#                 return
#     # return tempOrderList
#     ordersList.append(curr_order)
        
            
# def ShowOrderDetails(menus, ordersList):
#     for i in ordersList:
#         print(f"#Order number : {i['orderno']}") 

#         # print(f"{'Code':<10} {'Item Name':<15} {'Price':<10} {'Qty':<10} {'Total':<10}")
#         # print("-" * 57)

#         total = 0
#         for item in i['menus']:
#             # cost = item['price'] * item['quantity']
#             # total+=cost

#             print(f"{item['code']:<10} {item['qty']:<15} {item['status']:<10}")

#         print("-" * 55)
#         # print(f"Total {' '*42} {total}")
#         print()
    
    
    

#     # return ordersList 



def makeOrder(menus, ordersList):
    sr_no = len(ordersList)

    curr_order = {'orderno': sr_no, 'menus': []}

    customerOrder = input("Describe your order <menucode> <qty> :")
    # "M801 3, M804 2, M701 5"

    if isinstance(menus, list):
        codeList = [item['code'] for item in menus]
        co = [item.split(" ") for item in customerOrder.split(",")]
        # ['M801 3', 'M804 2', 'M701 5'] -> [['M801', '3'], ['M804', '2'], ['M701', '5']]

        tempOrderList = []
        for orderItem in co:
            d = dict()
            d['code'] = orderItem[0]
            d['qty'] = int(orderItem[1])

            if d['code'] in codeList:
                d['status'] = 'valid'
                print('Menu', d['code'], 'created order successfully')
            else:
                d['status'] = 'invalid'
                print('Menu', d['code'], 'does not exist. Try again')

            curr_order['menus'].append(d)  # Appending the valid order dictionary

        ch = input("Do you want to process this order [y/n]? :")
        if ch == 'y':
            # Ensure the order is only appended if it contains valid items
            if curr_order['menus']:
                ordersList.append(curr_order)  # Appending the valid current order to the orders list
        elif ch == 'n':
            ch1 = input('Modify/cancel order [m/c]? :')
            if ch1 == 'm':
                for eachItem in curr_order['menus']:
                    print("%20s %10d %10s" % (eachItem['code'], eachItem['qty'], eachItem['status']))

                    qty = int(input("Enter new quantity: "))
                    eachItem['qty'] = qty
                    if eachItem['qty'] == 0:
                        curr_order['menus'].remove(eachItem)

            elif ch1 == 'c':
                print("Your order is canceled")
                print("Thanks! Have a great day.")
                return


def ShowOrderDetails(menus, ordersList):
    for i in ordersList:
        
        if i is not None:  # Add a check to ensure i is not None
            print(f"#Order number: {i['orderno']}")
            print(f"{'code':<10} {'qty':<15} {'status':<10} {'Price':<10} {'Total':<10}")
            print("-" * 55)
            total = 0
            for item in i['menus']:
                menu = next(m for m in menus if m==item['code'] )
                # Display order details
                print(f"{item['code']:<10} {item['qty']:<15} {item['status']:<10} {item['price']:<10}  {cost:<10}")

            print("-" * 55)
            print()
        else:
            print("No valid order details to display.")


