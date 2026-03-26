
"""
──── Basic formatting (0-7) ────────────────────────────────────────────────────────────────── 
─ Used to change the style of the text in the terminal. 
─ Each style is represented by a specific escape code. 
─ I decided to add all of them but in the end i only used RESET, which is the most common one.
─ ANSI escape codes for text styling: \033 signals the terminal to read what follows as a
formatting instruction, [ opens it, the number sets the style, and m closes/applies it
"""
RESET   = "\033[0m" 
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
INVERT  = "\033[7m"

""" 
──── Text colors (30-37) ─────────────────────────────────────────────────────────────────────────────────────
─ Used to change the color of the text in the terminal. 
─ Each color is represented by a specific escape code. 
─ I decided to add all of them even if I only use a few, so I have them ready for future use (THIS IS NOT AI).
─ ANSI escape codes for text color: same structure as above, 3X where X is the color number (0-7)
"""
BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

# Main data structure — each product will be stored as a dictionary inside this list
Inventory = []
Option = None

# Reusable input function — keeps asking until the user enters a value that can be
# converted to the given type (default: str). Catches ValueError for invalid inputs
def get_info(prompt, type=str):
    im_not_true = None
    while im_not_true != "stop":               # Infinite loop to keep asking until valid input is received, 777 is just a fun number to use here SINCE YOU HATE WHEN WE USE "TRUE", it works the same way though
        try:
            return type(input(prompt))
        except ValueError:
            print(f"{RED}❌ Invalid input. Try again. ❌{RESET}\n")

# Add product — collects name, price and quantity, then appends a new dictionary to Inventory
def add_product():
    name     = get_info(f"{GREEN}~ Product name: {RESET}")
    price    = get_info(f"{GREEN}~ Price: {RESET}", float)
    quantity = get_info(f"{GREEN}~ Quantity: {RESET}", int)
    Inventory.append({"Product": name, "Price": price, "Quantity": quantity})

# Show inventory — loops through the list and prints each product in a formatted block.
# If the list is empty, notifies the user instead
def show_inventory():
    if not Inventory:
        print(f"{YELLOW}The inventory is currently empty.{RESET}\n")
    else:
        for product in Inventory:
            print(f"""{GREEN}— Product:  {product["Product"]}
Unit price: ${product["Price"]:.2f}
Quantity:   {product["Quantity"]}
{"─"*31}{RESET}""")

# Calculate statistics — computes total inventory value (price × quantity for all products)
# and total number of items using sum() with a generator expression.
# If the list is empty, notifies the user instead
def calculate_statistics():
    if not Inventory:
        print(f"{YELLOW}The inventory is currently empty. No statistics to show.{RESET}\n")
    else:
        total_value = sum(product["Price"] * product["Quantity"] for product in Inventory)
        total_items = sum(product["Quantity"] for product in Inventory)
        print(f"{GREEN}Total inventory value: ${total_value:.2f}{RESET}")
        print(f"{GREEN}Total number of items: {total_items}{RESET}")

# Main loop — keeps the program running until the user selects option 4 (Exit).
# Wraps the menu input in a try/except to handle non-integer inputs gracefully
will_of_god = 777
while will_of_god:
    try:    
        Option = int(input(f"""{BOLD}{MAGENTA}{"="*24}{RESET}{BOLD}{GREEN} MAIN MENU{RESET} {BOLD}{MAGENTA}{"="*25}{RESET}
{BOLD}{MAGENTA}1){RESET}{GREEN} 🩲​ Add product{RESET}
{BOLD}{MAGENTA}2){RESET}{GREEN} 📦​ Show inventory{RESET}
{BOLD}{MAGENTA}3){RESET}{GREEN} 🧾​ Calculate statistics{RESET}
{BOLD}{MAGENTA}4){RESET}{GREEN} 🔚​ Exit{RESET}
{BOLD}{MAGENTA}{"="*60}{RESET}
{BOLD}{GREEN}Choose an option:{RESET}
{MAGENTA}➤  {RESET}"""))

        # Option 1 — enters a sub-loop that keeps adding products until the user types 'exit'
        if Option == 1:
            Process = None
            while Process != "exit":
                print(f"{BOLD}{MAGENTA}{"="*23}{RESET}{BOLD}{GREEN} NEW PRODUCT{RESET} {BOLD}{MAGENTA}{"="*24}{RESET}")
                add_product()
                Process = input(f"{YELLOW}{ITALIC}Type 'exit' to return to the main menu, or press Enter to\nadd another product: {RESET}").lower()

        # Option 2 — displays all products currently stored in the inventory
        elif Option == 2:
            print(f"{BOLD}{MAGENTA}{"="*21}{RESET}{BOLD}{GREEN} SHOW INVENTORY{RESET} {BOLD}{MAGENTA}{"="*23}{RESET}")
            show_inventory()

        # Option 3 — shows total inventory value and total number of items
        elif Option == 3:
            print(f"{BOLD}{MAGENTA}{"="*23}{RESET}{BOLD}{GREEN} STATISTICS{RESET} {BOLD}{MAGENTA}{"="*25}{RESET}")
            calculate_statistics()

        # Option 4 — exits the program cleanly
        elif Option == 4:
            print(f"{GREEN}{"Exiting the program. Goodbye!".center(60)}{RESET}")
            exit()
        
        # Any other number — informs the user the option is out of range
        else:
            print(f"{BOLD}{RED}{"❌ ERROR: Please enter a number between 1 and 4. ❌".center(60)}{RESET}")

    # Non-integer input at the main menu — caught here so the program never crashes
    except ValueError:
        print(f"{BOLD}{RED}{"❌ ERROR: Please enter a valid input. ❌".center(60)}{RESET}")

"""
──── Summary ─────────────────────────────────────────────────────────────────────────
This program is a terminal-based inventory manager. It stores products as dictionaries
inside a list, and lets the user add products, browse the inventory, and view basic
statistics — all through a colored, interactive menu that runs until the user exits.
"""
