'''






Requirements
1. Show Menus to user
    Prettify the output in terminal/console and show user all menus iterating them using for loop 

2. User can able to make order to the available menus
        a. ask user to input following format of request to add menu in order
               M801 3, M804 2, M701 5      
               
               Note: 'M801' is menu-code and '3' is qtys and so on 
        
        b. validate the input
               Menu 'M801' created order successfully
               Menu 'M804' created order successfully
               Menu 'M701' not exist. try again
               
        c. Get user confirmation to process order
              if user input "y" then make an entry of order with following format in order-list
              format :[ {'orderno:0, 'menus':[
                            {'code':'M801', 'itemname':'sandwich', 'price':190, 'stock':True, 'qtys':3}}
                            {'code':'M804', 'itemname':'colddrink', 'price':50, 'stock':True, 'qtys':2}],
                            
                        {'orderno:1, 'menus':[
                            {'code':'M803', 'itemname':'burger', 'price':160, 'stock':True, 'qtys':5},}
                            {'code':'M805', 'itemname':'coffee', 'price':70, 'stock':True, 'qtys"7}]
                        }]                          
                    
                            
3. Show Orders Details seperated by order number with gross total in following format

    #Order number : 0
    M801    sandwich        190     3       570
    M804    colddrink       50      2       100
    ---------------------------------------------
    Total                                   670
    
    #Order number : 1
    -       -               -       -       -
    -       -               -       -       -
    ----------------------------------------------
    Total                                   -
                 
4. Calcualte and show Inventory followed by menus how many qtys sold and how much profit is made in following format
    
    Menu Name           IssuedQtys          Amount
    Sandwich                16              14000
    Pizza                   10              7000
    Burger                  41              17000
    Colddrink               13              600
    Coffee                  6               400
    Roll                    13              1500
    
    Total Amount in Profit is "xyz"
                           
'''