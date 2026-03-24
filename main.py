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

Option = None
try:    
    Option = int(input(f"""{BOLD}{MAGENTA}{"="*24}{RESET}{BOLD}{GREEN} MAIN MENU{RESET} {BOLD}{MAGENTA}{"="*25}  {RESET}
{BOLD}{MAGENTA}1){RESET}{GREEN} 🔍 Add product{RESET}
{BOLD}{MAGENTA}2){RESET}{GREEN} 💳 Show inventory{RESET}
{BOLD}{MAGENTA}3){RESET}{GREEN} 💰 Calculate statistics{RESET}
{BOLD}{MAGENTA}4){RESET}{GREEN} ✅ Exit{RESET}
{BOLD}{MAGENTA}{"="*60}{RESET}
{BOLD}{GREEN}Choose an option:{RESET}
{MAGENTA}➤  {RESET}""")) 
    if Option not in [1,2,3,4]:
        print(f"{BOLD}{RED}{"❌ ERROR: Please enter a number between 1 and 4. ❌".center(60)}{RESET}")
        Option = int(input(f"""{BOLD}{MAGENTA}{"="*24}{RESET}{BOLD}{GREEN} MAIN MENU{RESET} {BOLD}{MAGENTA}{"="*25}  {RESET}
{BOLD}{MAGENTA}1){RESET}{GREEN} 🔍 Add product{RESET}
{BOLD}{MAGENTA}2){RESET}{GREEN} 💳 Show inventory{RESET}
{BOLD}{MAGENTA}3){RESET}{GREEN} 💰 Calculate statistics{RESET}
{BOLD}{MAGENTA}4){RESET}{GREEN} ✅ Exit{RESET}
{BOLD}{MAGENTA}{"="*60}{RESET}
{BOLD}{GREEN}Choose an option:{RESET}
{MAGENTA}➤  {RESET}"""))
except ValueError:
    print(f"{BOLD}{RED}{"❌ ERROR: Please enter a valid input. ❌".center(60)}{RESET}")

if Option == 1:
    print("NOT IMPLEMENTED YET")
elif Option == 2:
    print("NOT IMPLEMENTED YET")
elif Option == 3:
    print("NOT IMPLEMENTED YET")
elif Option == 4:
    print("Exiting the program. Goodbye!")
    exit()