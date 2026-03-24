RESET   = "\033[0m" 
BOLD    = "\033[1m"
DIM     = "\033[2m"
ITALIC  = "\033[3m"
UNDER   = "\033[4m"
BLINK   = "\033[5m"
INVERT  = "\033[7m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

Inventory = []
Option = None

while 777:
    try:    
        Option = int(input(f"""{BOLD}{MAGENTA}{"="*24}{RESET}{BOLD}{GREEN} MAIN MENU{RESET} {BOLD}{MAGENTA}{"="*25}{RESET}
{BOLD}{MAGENTA}1){RESET}{GREEN} 🩲​ Add product{RESET}
{BOLD}{MAGENTA}2){RESET}{GREEN} 📦​ Show inventory{RESET}
{BOLD}{MAGENTA}3){RESET}{GREEN} 🧾​ Calculate statistics{RESET}
{BOLD}{MAGENTA}4){RESET}{GREEN} 🔚​ Exit{RESET}
{BOLD}{MAGENTA}{"="*60}{RESET}
{BOLD}{GREEN}Choose an option:{RESET}
{MAGENTA}➤  {RESET}"""))
        if Option == 1:
                Process = None
                while Process != "exit":
                    print(f"{BOLD}{MAGENTA}{"="*23}{RESET}{BOLD}{GREEN} NEW PRODUCT{RESET} {BOLD}{MAGENTA}{"="*24}{RESET}")
                    product_name = input(f"{GREEN}~ Product name: {RESET}")
                    unit_price   = float(input(f"{GREEN}~ Unit price: ${RESET}"))
                    quantity     = int(input(f"{GREEN}~ Quantity: {RESET}"))
                    subtotal     = unit_price * quantity
                    Product = {"Product": product_name, "Price": unit_price, "Quantity": quantity}
                    Inventory.append(Product)
                    print(f"{GREEN}{"Product added successfully!".center(60)}{RESET}\n")
                    Process = input(f"{YELLOW}{ITALIC}Type 'exit' to return to the main menu, or press Enter to\nadd another product: {RESET}").lower()

        elif Option == 2:
            print(f"{BOLD}{MAGENTA}{"="*21}{RESET}{BOLD}{GREEN} SHOW INVENTORY{RESET} {BOLD}{MAGENTA}{"="*23}{RESET}")
            if not Inventory:
                print(f"{YELLOW}The inventory is currently empty.{RESET}\n")
            
            for product in Inventory:
                print(f"""{GREEN}— Product:  {product["Product"]}
Unit price: ${product["Price"]:.2f}
Quantity:   {product["Quantity"]}
{"─"*31}{RESET}""")
        elif Option == 3:
            print("NOT IMPLEMENTED YET")
        elif Option == 4:
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print(f"{BOLD}{RED}{"❌ ERROR: Please enter a number between 1 and 4. ❌".center(60)}{RESET}")
    except ValueError:
        print(f"{BOLD}{RED}{"❌ ERROR: Please enter a valid input. ❌".center(60)}{RESET}")

