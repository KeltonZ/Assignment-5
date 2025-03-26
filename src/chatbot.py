"""This module defines the Chatbot application.

Allows the user to perform balance inquiries and make deposits to their 
accounts.

Example:
    $ python src/chatbot.py
"""

__author__ = "COMP-1327 Kelton Zinn"
__version__ = "1.0.2025"

ACCOUNTS = {
    123456: {
        "balance": 1000.0
    },
    789012: {
        "balance": 2000.0
    }
} 

VALID_TASKS = [
    "balance", 
    "deposit", 
    "exit"
]

## All the functions you add to the src.chatbot module will be inserted after the defined constants and before the chatbot() function.

def get_account_number() -> int:
    """
    Call function to request the user to input their account number,
    which will then be checked against the ACCOUNTS dict to validate,
    and will return value of result.

    User input must be digit or conversion will fail. 

    args:
        
        prompt = user account number input
        
        result =  prompt converted to int
    """
    prompt = input("Please enter your account number: ")
    if prompt.isdigit():
        result = int(prompt)
        if result in ACCOUNTS:
            return result
        else:
            raise ValueError("Account number entered does not exist.")
    else:
        raise TypeError("Account number must be an int type.")
    
def get_amount() -> float:
    """
    Requests deposit amount and runs exceptions when input is either not a float or int, ~
    ~ or if deposit is negative in value

    Args:
        deposit_input = float(input("Please enter amount: ")):
            
            This is equal to the value inputted by user, following the message prompt

        ValueError:
            If value is <= to zero exception will occur
        
        TypeError:
            If value is not int or float exception will occur
    """
    try:
        deposit_input = float(input("Please enter amount: "))
        if deposit_input <= 0:
            raise TypeError("Amount must be a value greater than zero.")
        else:
            return deposit_input
    #Had to invert the Value and type error function as I could not figure out another method and baseline was always ValueError for TypeError entry
    except ValueError as e:
        raise ValueError("Amount must be a numeric type.") from e

def get_balance(account_number: int) -> float:
    """References get_account_num function and accesses relative key-value pair then prints current balance"""
    account_number = get_account_number()
    account_balance = ACCOUNTS[account_number]['balance']
    return f"Your current balance for account {account_number} is {'${:,.2f}'.format(account_balance)}"

def make_deposit(account_number: int, amount: float):
    account_number = get_account_number()
    amount = get_amount()
    return f"You have made a deposit of {'${:,.2f}'.format(amount)} to account {account_number}"

def chatbot():
    """Performs the Chatbot functionality."""
    COMPANY_NAME = "PiXELL River Financial"

    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")

    # Print thank you message
    print(f"Thank you for banking with {COMPANY_NAME}.")

if __name__ == "__main__":
    chatbot()
