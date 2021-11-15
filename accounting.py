from user import authentication
from transactions import journal
import banking
import sys


def main():
    if authentication.authenticate_user():
        journal.receive_income(100)
        journal.pay_expense(100)
        banking.reconciliation.do_reconciliation()


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(arg)
    # help("modules") 
    main()