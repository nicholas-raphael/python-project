from rich import print
from rich.prompt import Prompt
from bank import Bank_Account
CHOICES=["test", "deposit", "withdraw", "display"]

def main():
    s = Bank_Account()
    
    while True:
        option = Prompt.ask("Escoge una opcion", choices=CHOICES, default="test")
        if option == "test":
            pass
        if option == "deposit":
            s.deposit()
        if option == "withdraw":   
            s.withdraw()
        if option == "display":
            s.display()

if __name__ == "__main__":
    main()