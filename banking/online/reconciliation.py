import requests
print("[Module] online.Reconciliation loaded.")

def do_reconciliation():
    """
    Does online reconciliation, whatever that is
    requests a response from 'https://www.wethinkcode.co.za'
    in the process.
    prints the response
    """
    print("Doing Online Bank reconciliation.")
    response  = requests.get('https://www.wethinkcode.co.za')
    print(response.status_code)
