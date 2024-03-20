import getpass # hides passwords. also used to "pause" the terminal until enter is pressed
import json # allows use of .json files
from random import randint # Required to pick a random item to add to cart
#from classes import Cart, Customer # Sadly couldn't get this or import of functions to work before deadline...
#from functions import *  

 
class Cart:
    def __init__(self, customer_number): # initialises a cart instance 
        self.items = [] # create an empty list
        self.total_price = 0.0 # set total price to 0
        self.customer_number = customer_number # saves customer number to cart

    def add_item(self, item, amount): # function that adds items to cart by having said item and amount as positional arguments
        
        if amount == 1: # if only one item is added
            self.items.append(item) # append items to cart
            self.total_price += item['item_price'] # increase total price of cart
            print(f"{item['item_name']} added to cart. Cost: {item['item_price']}$") # prints what item was added and what it costs

        if amount > 1: # if several items are added
            counter = 0 # create a counter
            while counter < amount: #w hile loop to add several items
                self.items.append(item) # append item to cart
                self.total_price += item['item_price'] # increase total price of cart
                counter += 1 # increase counter
            print(f"{amount}x {item['item_name']} added to cart. Cost: {item['item_price']}$ x {amount} = {round((item['item_price']* amount), 2)}$")
            #print an f-string telling what amount of what items was added and the costs of these. Rounds item_price to two decimals because floats can have really many decimals
        
        

    def remove_item(self, item, amount): # function that removes items from cart
        if amount == 1: # if only one item should be removed
            self.items.remove(item) # remove item from cart
            self.total_price -= item['item_price'] # deduct items price from total price of cart
            print(f"{item['item_name']} removed from cart.") # prints what item was removed
 
        if amount > 1: #if several items should be removed from cart. Same principal as add_items above, use for reference 
            counter = 0
            while counter < amount:
                self.items.remove(item)
                self.total_price -= item['item_price']
                counter += 1
            print(f"{amount}x {item['item_name']} removed from cart.")

    def empty_cart(self): # empties cart
        self.items = [] # sets list to be an empty list
        self.total_price = 0.0 # set carts price to 0
        print("\nCart emptied!")
        press_enter()
    
    def to_checkout(self, cart_list, customer_number, customer_name): # takes info about current order and prepares it for checkout (to be added to json)
        order_info = {
        "customer_number": customer_number,
        "customer_name": customer_name,
        "cart": cart_list,
        "cart_price": self.total_price
        }
        return order_info 

class Customer:

    def __init__(self, customer_number, customers): # gets customer_number and customers (loaded from json) to initialise customer with customer data
        customer_data = {} # create empty dictionary
        for customer in customers: # iterate customers. 

            if customer['customer_number'] == customer_number: # if inputted customer_number matches a customers number:

                customer_data = customer # set customer_data to that customers data
                break # breaks for-loop when customer is found
        

        # Set instance variables based on the customer data
        self.number = customer_number
        self.name = customer_data['customer_name']
        self.password = customer_data['customer_password'] 
   




# ------------------- Misc functions ----------------------------
# "Quality of life" functions. Formats what's output to the terminal for better presentation.

def clear(): # "clears" the terminal by printing a bunch of new lines
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def press_enter(): # stops the terminal from printing further, giving the user time until they are ready to proceed
    getpass.getpass("\nPress Enter to continue.")
    clear() # then clears the terminal

def print_foodexpress_ascii(): # prints the FoodExpress banner in ascii art
    print('''
----------------------------------------------------------------------------------
| #######                      #######                                           |
| #        ####   ####  #####  #       #    # #####  #####  ######  ####   ####  |
| #       #    # #    # #    # #        #  #  #    # #    # #      #      #      |
| #####   #    # #    # #    # #####     ##   #    # #    # #####   ####   ####  |
| #       #    # #    # #    # #         ##   #####  #####  #           #      # |
| #       #    # #    # #    # #        #  #  #      #   #  #      #    # #    # |
| #        ####   ####  #####  ####### #    # #      #    # ######  ####   ####  |
----------------------------------------------------------------------------------    ''')

def print_admin_ascii(): # prints the Admin banner
    print('''
----------------------------------------
|    #    ######  #     # ### #     #  |
|   # #   #     # ##   ##  #  ##    #  |
|  #   #  #     # # # # #  #  # #   #  |
| #     # #     # #  #  #  #  #  #  #  |
| ####### #     # #     #  #  #   # #  |
| #     # #     # #     #  #  #    ##  |
| #     # ######  #     # ### #     #  |
----------------------------------------
    ''')

def format_cart_list(cart_list): # takes cart_list [list with all items in cart] and prints a nice formated list of what items cart contains
    current_item_number = 1 
    while current_item_number <= len(items): # go through all item numbers to count each of the items which might be in cart
        item_amount = cart_list.count(current_item_number) # counts current item number in cart
        if item_amount > 0:
            
                for item in cart.items: # iterates items in cart
                    item_number = item["item_number"]
                    item_name = item['item_name']
                    item_price = item['item_price']

                    if item_number == current_item_number: # compares the item number currently being "scanned" to item in carts item number, if match: print amount, item, price and total price
                        print(f"{item_amount}x\t{item_name}\t\t{item_price}$ x {item_amount} = {round(item_price * item_amount, 2)}$ ")
                        break
                
            
        current_item_number+=1 # increase item number by one to check next item

# ------------------- Initial functions --------------------------------
# Load from json files, login function

def load_items(): #loads json file containing all items and their information 
    with open('items.json') as f: # open items.json
        data = json.load(f) # loads content of items.json into variable called "data"

    items = data['items'] # reads all items and adds to variable called items
    return items

def load_customers(): # loads json file containing all customer information. Same principle as function above, see for reference
    
    with open('customers.json') as f: 
        data = json.load(f) 

    customers = data['customers'] 
    return customers
    
def load_orders(): # loads json file containing order history. Same principle as function above, see for reference
    with open('orders.json') as f: 
        data = json.load(f)

    orders = data
    return orders


def login(customers): # enter customer number or name, asks for password, returns customer number 
    print_foodexpress_ascii()
    while True: 
        try:
            customer_input = input("Welcome to FoodExpress.\nPlease enter your customer number: ") 
            customer_input = customer_input.lower() # to not care about capitalization
            
            for customer in customers: # iterate customers
                if customer_input == customer['customer_name']: # if input customer data matches with customer_name in json
                    customer_input = customer['customer_number'] # change customer_input to customer number instead. Needed for list index
                
            
            customer_input = int(customer_input) #needs to be int for list index

            password = getpass.getpass(prompt="Enter your password: ") # enter your password

            while True: # check password to ensure it's correct
                customer_test = customers[customer_input] # set customer_test to be able to check what customer_password is stored
                customer_password = customer_test['customer_password']

                if password == customer_password: # if password is correct, break loop and proceed
                    break
                                    
                else: # if password is incorrect, try again.

                    password = getpass.getpass(prompt="Invalid password. Please try again: ")

            
            
            customer_input = str(customer_input) # needs to be str later so converting already
            return customer_input
        
        except ValueError:
            clear()
            print(f"Customer {customer_input} does not exist. Try again.\n") # if customer_number doesn't exist, don't crash the application



# ----------------------------- Menu choices ---------------------------------------------------------

def list_items(): # lists all items in assortment
    clear()
    print_foodexpress_ascii()
    print(f"Assortment and prices.\n\n#:\tItem:\tPrice:\t")
    for item in items: # iterate items 
        print(f"{item['item_number']}\t{item['item_name']}\t{item['item_price']}$") # print iterated items item information
    

def list_cart(): # list contents of cart
    clear()
    print_foodexpress_ascii()
    if cart.total_price > 0.0: # if cart contains something
                
                cart_list = create_cart_list() # create a list containing all items cart contains (by item number)
                    
                print("\nCurrent cart:\n")
                print(format_cart_list(cart_list)) # format the list of what items cart contains for better presentation
                
                
                print(f"Total price: {round(cart.total_price, 2)}$") # round() to prevent many decimals from float

    else: # if cart is empty, go back to main menu. Nothing to list, add something.
        print("\nCart is empty. Try adding something!")

def create_cart_list(): # check what cart contains and make a list out of it. 
    cart_list = [] # create empty list
    for item in cart.items: # iterate items in cart
        item_number = item["item_number"] # set current item as item_number
        cart_list.append(item_number)  # append the list with this item_number
    return cart_list


def add_random_item():
    clear()
    print_foodexpress_ascii
    total_amount_items = len(items) # counts how many items are in items so it knows max amount of randint()
    random_choice = randint(1, total_amount_items) # generate random number between 1 and length of list of items
    random_choice-=1 # to match list index that starts with 0
    print_foodexpress_ascii()
    print(f"\nAdding random item to cart!\n")
    cart.add_item(items[random_choice], 1) # add 1x of random item and go back to main menu
    press_enter()

def add_to_cart(): # add an item to cart
    clear()
    
    while True:
                    print_foodexpress_ascii()
                    list_items() # list assortment
                    list_cart() # list current cart
                    user_input = str(input("\nAdd items to cart. Input the items number or name.\nOther commands: list, cart, random, quit.\n: ")) # input what should be added to cart
                    user_input = user_input.title() # if item_name is input,makes sure it's matching capitalization with statements in next section

                
                    while user_input == "Cart" or user_input == "C": # if Cart is input in menu, list cart
                        list_cart()
                        user_input = input("\nAdd items to cart. Input the items number or name.\nOther commands: list, cart, random, quit.\n: ") # then ask for input
                        user_input = user_input.title() 

                    while user_input == "List" or user_input == "Ls" or user_input == "L": # if list is input in menu, list all items
                        list_items()
                        user_input = str(input("\nInput the items number or name: ")) # input what should be added
                        user_input = user_input.title()

                    if user_input == "Random" or user_input == "R": # adds random item to cart
                        add_random_item()
                        break

                    if user_input == "Q" or user_input == "Quit" or user_input == "0": # quit to main menu
                        print("\nCancelling and going back to main menu.")
                        press_enter()
                        break
                    
                                                                            
                    item_amount = input(str("How many?: ")) # amount of item to be added to cart
                    print("") # just for formatting, wanted a "break line" here
                    
                    if item_amount == "Q" or item_amount == "Quit" or item_amount == "0": # quit to main menu, even after an item to add has been input (now asking for amount)
                        print("\nCancelling and going back to main menu.")
                        press_enter()
                        break
                    
                    if isinstance(user_input, str): #Checks if string, if so, find the item number of item
                        for item in items: # iterate items
                            if item['item_name'] == user_input: # if an items name matches the user input:
                                user_input = item['item_number'] # change input to its item number

                    user_input = int(user_input) 
                    item_amount = int(item_amount)
                    

                    
                    
                    user_input -= 1 # adjust as index starts at 0 and not 1

                    cart.add_item(items[user_input], item_amount) # add X items to cart

                    press_enter()    

def remove_from_cart(): # remove items from cart, clear cart
    while True:
        if cart.total_price == 0: # if there's nothing in cart, go back to main menu
            clear()
            print_foodexpress_ascii()
            print("\nCart is already empty, try adding something first.")
            press_enter()
            return
        print_foodexpress_ascii()
        list_cart()

        user_input = user_input = str(input("\nRemove items from list. Input the items number or name.\nOther commands: empty, quit.\n: ")) # select what item will be removed
        user_input = user_input.title() # to match capitalization of statements below

        if user_input == "Quit" or user_input == "Q": # go back to main menu
            print("\nQuitting to main menu.")
            press_enter()
            break

        if user_input == "Empty" or user_input == "E": # Empties cart of all items
            cart.empty_cart() 
            break

        elif isinstance(user_input, str): #Checks if string, if so, find the item number of item
            for item in items:
                if item['item_name'] == user_input: # if item_name of item matches user_input
                    user_input = item['item_number'] # change user_input to item_number instead


        item_amount = input("How many?: ") # specify amount of said item to be removed

        user_input = int(user_input) 
        item_amount = int(item_amount)
        

        
        
        user_input -= 1 # adjust as index starts at 0 and not 1

        cart.remove_item(items[user_input], item_amount) # removes X items from cart

        press_enter() 
        clear()
            
def checkout(): # check out items in cart, add to orders.json
    clear()
    print_foodexpress_ascii()

    if cart.total_price == 0: # if cart empty, nothing to check out. Go back to main menu.
        print("\nCart is empty, nothing to check out. Try adding something first!")
        press_enter()
    else:
        while True:
            list_cart()
            password = getpass.getpass(prompt="\nAre you sure you want to check out this cart?\nPlease enter your password to confirm, or q to go back to menu: ")
            
            if password == customer.password: # check password to confirm check out of cart
                clear()
                print_foodexpress_ascii
                cart_list = create_cart_list() # get items from cart and add to a list
                order_info = cart.to_checkout(cart_list, customer_name=customer.name, customer_number=customer.number) # prepare order info for checkout
                orders.append(order_info) # append order info to list of orders orders

                with open('orders.json', 'w') as f: # write order info to orders.json
                    json.dump(orders, f, 
                    indent=4,  
                    separators=(',',': '))
                cart.empty_cart() # empty cart
                break # go back to main menu

            password = password.lower()
            if password == "q" or password == "quit" or password == "n" or password == "no": # if input is quit, exit to main menu
                print("Exiting to main menu")
                break
            
            else:
                print("Invalid password, please try again.")

def customer_history(): # prints only the current customers order history, sorted after total order value. To print all customers orders, go to admin menu
    print_foodexpress_ascii()
    sorted_orders = sorted(orders, key=lambda x: x['cart_price'], reverse = True) # takes the dicttionary orders and sorts it after cart_price
    print("Not formatted for a nice output, but technically orders have been listed sorted after total order value\n(Shows only current customers history, for all customer history, go to admin menu. For customer privacy.)") 
    for order in sorted_orders:
        if order['customer_number'] == customer_number: # if current customer matches an orders customer_number:
            print(order) # print each order 
    press_enter()

def list_customer_information(): # Lists customer information. 
    clear()
    print_foodexpress_ascii()
    print(f"Customer number: {customer.number}\nCustomer name: {customer.name.title()}\nPassword: {customer.password}")
    press_enter()

def print_customers_by_spending(orders): # takes order history, counts total value of all orders by customer and sorts them by biggest spender
    customers_spending = {} # creates empty dictionary

    # Iterate through each order and add up the cart_price values for each customer
    for order in orders:
        customer_number = order['customer_number']
        cart_price = order['cart_price']
        if customer_number in customers_spending:
            customers_spending[customer_number] += cart_price
        else:
            customers_spending[customer_number] = cart_price

    # Sort the customers based on their total spending in descending order
    sorted_customers = sorted(customers_spending.items(), key=lambda x: x[1], reverse=True)

    # Print the customers in order of their total spending
    for customer in sorted_customers:
        print(f"Customer with customer number {customer[0]} has spent a total of {round(customer[1], 2)}$")

def admin_menu(): # admin menu. contains list of biggest spenders and all customer orders. Structure in here is messy because time was running out, I hope normal menu cleanliness can make up for it.
    
    while True:
                    clear()
                    print_admin_ascii()
                    print ('''
------- Admin Menu ------- 
1. List biggest spenders
2. List all orders (Sorted after total order value)
q. Quit to main menu
                    ''')

                    choice = str(input("Select a menu option: "))
                    choice = choice.lower() # for all variations of capitalization on q / quit

                    if choice == "1":
                        clear()
                        print("Biggest spenders:")
                        print_customers_by_spending(orders) # takes orders and sends them to print_customers_by_spending, which iterates orders and adds up them based on which customer they belong to

                    elif choice == "2": # List all customer orders sorted after cart value
                         clear()
                         sorted_orders = sorted(orders, key=lambda x: x['cart_price'], reverse = True) # Sorts all orders after cart_price (total value of cart) 
                         print("Not formatted for a nice output, but technically orders have been listed sorted after total order value")
                         for order in sorted_orders:
                            print(order) # prints all orders sorted after cart_price
                    
                         
                    
                    elif choice == "0" or choice == "q" or choice == "quit": # quit to main menu
                        print("\nQuitting to main menu.")
                        press_enter()
                        break

                    else:
                        print("Invalid input, please try again")

                    press_enter()




def menu(): # main menu function
    if customer.number == "0": # greets Admin with a special message
        clear()
        print_admin_ascii()
        print("Logged in as an administrator account! Extra functionality unlocked.")

    print(f"\nWelcome {customer.name.title()}!") # welcomes whichever user logs on
    press_enter()
    clear()

    while True: 

        try: # Catches errors and returns to main menu
            print_foodexpress_ascii()
            print(f'''
   ------- Menu ------- 
1. Assortment & Prices
2. Show current cart
3. Add to cart
4. Add random item to cart
5. Remove from cart
6. Checkout 
7. Customer order history
8. x
9. Show customer information (Logged in as {customer.name.title()})
q. Log out''') # Prints the main menu. 
            if customer.number == "0": # Show option for admin menu if logged in as admin
                print("a. Admin menu")

            choice = str(input("\nSelect a menu option: "))
            choice = choice.lower() # if choice is string, make lower so always same capitalization
            
            if choice == "1": # Assortment and prices. List item_numbers, items and prices.
                list_items()
                press_enter()
                

            elif choice == "2": # List current cart. 
                list_cart()
                press_enter()


            elif choice == "3": #Add to cart. Enter item_number / ls assortment / add random item to cart
                add_to_cart()

            elif choice == "4" or choice == "r" or choice == "random":
                add_random_item()

            elif choice == "5": # Remove from cart , show cart, Empty cart
                remove_from_cart() 
            
            elif choice == "6": # Checkout, write to file, empty cart
                checkout()
            
            elif choice == "7": #Order history, lists only current customer for customer privacy. Log in as admin to see all customer orders
                customer_history()

            elif (choice == "8" or choice == "a" or choice == "admin" or choice == "adm") and customer.number == "0": # admin menu with the list of biggest spenders. Can only be accessed by admin
                admin_menu()

            elif (choice == "8" or choice == "a" or choice == "admin" or choice == "adm") and customer.number != "0": # if a non-admin tries to access admin menu
                clear()
                print("\nERROR: Invalid choice. Try again!")
            

            elif choice == "9": # show customer information
                list_customer_information()

            

            elif choice == "0" or choice == "q" or choice == "quit": #Log out, exit application
                print("\nYou logged out. See you next time!\n")
                break

            
                
        
        except ValueError: #Catches error, prints and then goes back to main menu
            clear()
            print("\nERROR: Invalid choice. Try again!")
        
        clear()






# main "body" of code

clear()
items = load_items() # loads items from items.json
customers = load_customers() # loads customers from customers.json
customer_number = login(customers) # log in, returns customer_number when verified customer_number belongs to you
orders = load_orders() # load order history from orders.json




customer = Customer(customer_number, customers) # initiates instance of Customer, sets customer.variables
cart = Cart(customer_number) # initiates an instance of Cart, send customer number to cart, sets cart.variables


menu() # runs main menu until break
