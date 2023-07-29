
import sys

#========The beginning of the class==========
class Shoe:


    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quatity

    def __str__(self):
        return f'''Country: {self.country}, Code: {self.code}, Product: {self.product}, Code: R{self.cost}, Quantity: {self.quantity}'''

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt and read 
    the data from this file, then create a shoes object with 
    this data and append this object into the shoes list.
    '''
    try:

        with open("inventory.txt", "r") as file:
            next(file) # This will skip the first line on the file

            # Clearing the list so that is does not double everytime this
            # fucntion is called consecutively
            shoe_list.clear()
            
            for line in file:
                # Converting the string into a list
                line = line.strip().split(",")

                # Creating a shoe object from the lines in the inventory.txt
                # file
                line = Shoe(line[0], line[1], line[2], line[3], line[4])

                # Adding each read object into the shoe_list
                shoe_list.append(line)

        print("Shoe list has successfully refreshed!\n")

    except Exception as e:
        print(f"Oops! {e}")


def capture_shoes():
    '''
    Allows a user to capture data about a shoe and use 
    this data to create a shoe object and append this 
    object inside the shoe list.
    '''    

    print("\n========== CAPTURE A NEW SHOE ==========")
    # Getting the user input
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")

    # Creating a new shoe object from user input
    shoe = Shoe(country, code, product, cost, quantity)

    # Adding the new shoe to shoe_list
    shoe_list.append(shoe)

    # Writing the new shoe object to the inventory.txt file
    with open("inventory.txt", "a") as file:
        file.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}")

    print(f"\nThe '{shoe.product}' has been successfully captured and added to inventory.txt\n")


def view_all():
    '''
    Iterates over the shoes list and prints the details of the 
    shoes returned from the __str__ function.
    '''
    print("\n========== LIST OF ALL SHOES ==========")

    for number, shoe in enumerate(shoe_list, start=1):
        print(number, shoe)
    print()


def re_stock():
    '''
    Finds the shoe object with the lowest quantity so that the user
    re-stock it.
    '''    
    try:
        with open("inventory.txt", "r") as file:
            next(file) # This will skip the first line on the file

            # Convert the file into a list
            new_list = [line.strip().split(",") for line in file]

            # Convert the string quantity into an integer
            new_list = [[line[0], line[1], line[2], line[3], int(line[4])] for line in new_list]

            # Sorting the list by quality in ascending order so that we
            # can have the smallest shoe quantity at the first index
            new_list.sort(key=lambda x: x[4])

            lowest_quantity = new_list[0]

            print("\n========== ITEM RE-STOCK ==========")
            
            answer = input(f"Do you want to add {lowest_quantity[4]} shoes to {lowest_quantity[2]}? (y/n) ")
            # if the user wants to add the quantity of shoes
            if answer.lower() == 'y':
                
                # update the quantity of shoes
                lowest_quantity[4] *= 2

                # openning the text file in write mode
                with open("inventory.txt", 'w') as f:
                    f.write("Country,Code,Product,Cost,Quantity\n")

                    # Writing the updated shoe quantity to the inventory.txt file
                    for shoe in new_list:
                        f.write(','.join(str(x) for x in shoe) + '\n')
                print(f"{lowest_quantity[4] // 2} shoes added to {lowest_quantity[2]}\n")
            else:
                print("No shoes were added.")

    except Exception as e:
        print(f"Oops! {e}")

    
def search_shoe():
    '''
     Searches for a shoe from the list using the shoe code 
     and return this object so that it will be printed.
    '''    
    try:
        print("\n========== SEARCH SHOE BY CODE ==========")

        shoe_code = input("Enter the shoe code for the shoe you want to search: ")

        for shoe in shoe_list:
            if shoe.code == shoe_code:
                print(f"\n========== THE {(shoe.product).upper()} SHOE ==========")
                print(f"{shoe}\n")
    
        return f"No shoe was found with the code {shoe_code}.\n"
    
    except Exception as e:
        print(f"Oops! {e}")
    

def value_per_item():
    '''
    Calculates the total value for each item (value = cost * quantity),
    then prints this information on the console for all the shoes.
    '''    
    print("\n========== THE TOTAL VALUE FOR EACH SHOE ==========")
    
    for shoe in shoe_list:
        value = float(shoe.cost) * int(shoe.quantity)

        # Formatting the value to look like money
        value = "R{:,.2f}".format(value)
        
        print(f"{shoe.product} is: {value}")
    print()


def highest_qty():
    '''
    Determines the product with the highest quantity and
    prints it as being for sale.
    '''
    # Sorting the list by quantity
    shoe_list.sort(key=lambda x: int(x.quantity))

    # Setting the last item in the list as the max_quantity 
    max_quantity = shoe_list[-1]

    print(f'''\n========== 50% SALE NOW ON !!! ==========
    Product: {max_quantity.product}
    WAS: R{max_quantity.cost}
    NOW: R{int(max_quantity.cost) / 2}\n''')


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

while True:
    
    try:
        #Refreshing the shoe_list
        read_shoes_data()

        menu = input('''========== MAIN MENU ==========
        1. View all shoes.
        2. Capture a new shoe.
        3. Re-stock.
        4. Search shoe by code.
        5. View value of shoes.
        6. See what's on sale
        7. Exit
    
        Enter selection: ''')

        if menu == "1":
            view_all()

        elif menu == "2":
            capture_shoes()

        elif menu == "3":
            re_stock()

        elif menu == "4":
            search_shoe()

        elif menu == "5":
            value_per_item()

        elif menu == "6":
            highest_qty()

        elif menu == "7":
            print("\nBye for now!\n")
            # Exiting the program
            sys.exit(1)

        else:
            raise Exception(f"'{menu}' is not a valid entry. Please try again.\n")

    except Exception as e:
        print(f"\nOops! {e}")
