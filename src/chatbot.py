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
            #print(str(result)) #used to confirm output while writing
            return result
        else:
            raise ValueError("Account number entered does not exist.")
    else:
        raise TypeError("Account number must be an int type.")
    

        
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
