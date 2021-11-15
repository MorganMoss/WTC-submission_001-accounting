from user import authentication
from transactions import journal
import banking
import sys


def main():
    """
    Main function, checks if the user is authenticated then
    does some random bank stuff idk (well I do, but ya know)
    reveives and pays a random number then does reconciliation
    """
    if authentication.authenticate_user():
        journal.receive_income(100)
        journal.pay_expense(100)
        banking.reconciliation.do_reconciliation()


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(arg)
    # help("modules") 
    main()