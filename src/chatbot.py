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
    if prompt.isdigit():     #should have written as: if prompt != str(ACCOUNTS): raise TypeError 
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
    """References get_account_num function and accesses relative key-value pair then prints current balance
    
    Args:
    account_number:
        converted to integer, will pass value to get_account_number function

    account_balance:
        returns the balance value of whatever key was referenced in the ACCOUNTS dictionary from the get_account_number function
    """
    account_number =  get_account_number()
    account_balance = ACCOUNTS[account_number]['balance']
    return f"Your current balance for account {account_number} is {'${:,.2f}'.format(account_balance)}"

def make_deposit(account_number: int, amount: float):
    """returns the total deposited amount referenced from the get_amount input
    
    Args:
    
    account_number:
        converted to integer, will pass value to get_account_number function
         
    amount:
        passes the value to get_amount function and returns deposit statement
    """
    account_number = get_account_number()
    amount = get_amount()
    return f"You have made a deposit of {'${:,.2f}'.format(amount)} to account {account_number}"

def get_task():
    """"Used to request input from user, and validate against different functions, then calls those functions"""
    task_prompt = input("What would you like to do (balance/deposit/exit)?: ")
    task_prompt = task_prompt.lower()
    if task_prompt != "balance" and task_prompt != "deposit" and task_prompt != "exit":
        raise ValueError(f'"{task_prompt}" is an unknown task.') 
    if task_prompt == "balance":
        task_prompt = get_balance(account_number = str)
        print(task_prompt)
        return task_prompt   
    if task_prompt == "deposit":
        return task_prompt
    elif task_prompt == "exit":
        return task_prompt
    



def chatbot():
    """Performs the Chatbot functionality.
    
    is used to take existing functions, and calls them to perform menu functionality

    Args:
        junction_1:
            This is used as a junction point for when a process is completed, to avoid the chatbot spamming the user~
            ~with the welcome message.
    Notes:
    Essentially each function is called based on the input of the user, and all exceptions are handled by returning~
    ~a statement and then printing that statement, followed by calling junction_1.

    All functions call junction_1 once their task is completed except for exit which ends the loop with a goodbye message.

    final statement can't be balance or else the code wont call junction_1 and will simply end the program function, if I were to recode this~
    ~I might consider coding so that exit is along the same if line rather than adding useless code.

    """
    COMPANY_NAME = "PiXELL River Financial"
    
    # Print welcome message
    print(f"Welcome! I'm the {COMPANY_NAME} Chatbot! "
          f"Let's get chatting!")
    def junction_1():
        try:
            task = get_task()  
            if task != "exit":
                if task == "deposit":
                    task = make_deposit(account_number = str, amount=float)
                    print(task)
                    junction_1()          
                elif task == "balance":
                    task = get_balance(account_number = str)
                    print(task)
                    junction_1() #code wont iterate?
                else:
                    junction_1()           
            else:
                print(f"Thank you for banking with {COMPANY_NAME}.") # Print thank you message
                return
        except TypeError as te:
            print(te)
            junction_1()
        except ValueError as ve:
            print(ve)
            junction_1()
    junction_1()        

if __name__ == "__main__":
    chatbot()
    