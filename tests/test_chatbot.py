"""This module defines the TestChatbot class.

The TestChatbot class contains unit test methods to test the 
src.chatbot.Chatbot class.

You must execute this module in command-line where your present
working directory is the root directory of the project.

Example:
    python -m unittest tests/test_chatbot.py
"""

__author__ = "COMP-1327 Kelton Zinn"
__version__ = "1.0.2025"
import unittest
from unittest import TestCase, main
from unittest.mock import patch
from src.chatbot import ACCOUNTS, VALID_TASKS
from src.chatbot import get_account_number, get_amount, get_balance, make_deposit, get_task


class Testchatbot(unittest.TestCase):
    def test_get_account_number_type_error(self):
        """ Tests the TypeError exception handling"""
        # Arrange
        with patch('builtins.input', side_effect=["one"]):
        
        # Act & Assert
            with self.assertRaises(TypeError) as context:
                get_account_number()
            self.assertEqual(str(context.exception), "Account number must be an int type.")

    def test_get_account_number_value_error(self):
        """Tests the ValueError exception handling"""
        # Arrange
        with patch('builtins.input', side_effect=["123"]):
            #Act & Assert
            with self.assertRaises(ValueError) as context:
                get_account_number()
            self.assertEqual(str(context.exception), "Account number entered does not exist.")

    def tests_get_account_number_account_exists(self):
        """"Tests the account validation step"""
        # Arrange
        account_exists = 123456
        with patch('builtins.input', side_effect=[str(account_exists)]):
            # Act
            result = get_account_number()
            # Assert
            self.assertEqual(result, account_exists)
    
    def test_get_amount_not_numeric(self):
        """Tests exception handling when input is not numeric"""
        # Arrange
        with patch('builtins.input', side_effect=["e"]):
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Amount must be a numeric type.")
    
    def test_get_amount_is_equal_or_lesser_than_zero(self):
        """Test exception handling when input is <= zero"""
        # Arrange
        with patch('builtins.input', side_effect=["-12", "0"]):
            # Act & Assert
            with self.assertRaises(TypeError) as context:
                get_amount()
            self.assertEqual(str(context.exception), "Amount must be a value greater than zero.")
    
    def test_get_amount_valid_amount(self):
        """Test to confirm valid amounts, both int and floats converting to float"""
        # Arrange
        valid_amount_int = "100"

        valid_amount_float = "12.1"
        
        valid_output_int = 100.0

        valid_output_float = 12.1

        with patch('builtins.input', side_effect=[valid_amount_int, valid_amount_float]):
            # Act
            result = get_amount()
            # Assert
            self.assertEqual(result, valid_output_int, valid_output_float)

    def test_get_balance_param_not_int(self):
        """Confirming TypeError exception handling when input is not int"""
        # Arrange
        account_number = "one"
        with patch('builtins.input', side_effect=[account_number]):
        
        # Act & Assert
            with self.assertRaises(TypeError) as context:
                get_balance(account_number)
            self.assertEqual(str(context.exception), "Account number must be an int type.")
        
    def test_get_balance_account_does_not_exist(self):
        """Tests ValueError exception handling when account number does not match dictionary key"""
        # Arrange
        account_number = "123"
        with patch('builtins.input', side_effect=[account_number]):

        # Act & Assert
            with self.assertRaises(ValueError) as context:
                get_balance(account_number)
            self.assertEqual(str(context.exception), "Account number entered does not exist.")
    
    def test_get_balance_valid(self):
        """Tests valid account numbers"""
        # Arrange
        account_number_1 = "123456"
        account_number = 123456
        account_balance = 1000.0

        expected = f"Your current balance for account {account_number} is {'${:,.2f}'.format(account_balance)}"

        #account_balance_2 = "Your current balance for account 789012 is $2,000.00"

        # Act & Assert
        with patch('builtins.input', side_effect=[account_number_1]):
            # Act
            result = get_balance(account_number_1) 
            
            # Assert
            self.assertEqual(result, expected)    
    
    def test_make_deposit_not_int_type(self):
        """Tests TypeError for account number input"""
        # Arrange
        account_number = "e"
        with patch('builtins.input', side_effect=[account_number]):
        
        # Act & Assert
            with self.assertRaises(TypeError) as context:
                make_deposit(int, account_number)
            self.assertEqual(str(context.exception), "Account number must be an int type.")

    def test_make_deposit_not_in_dictionary(self):
        """" Testing ValueError for ACCOUNTS key"""
        # Arrange
        account_number = "12345"
        with patch('builtins.input', side_effect=[account_number]):
            #Act & Assert
            with self.assertRaises(ValueError) as context:
                make_deposit(int, account_number)
            self.assertEqual(str(context.exception), "Account number entered does not exist.")
    
    def test_make_deposit_lesser_or_equal_zero(self):
        """"Testing TypeError when lesser than or equal to zero for amount"""
        # Arrange
        account_number = "123456"
        amount = "-12"
        with patch('builtins.input', side_effect=[account_number, amount]):
            # Act & Assert
            with self.assertRaises(TypeError) as context:
                make_deposit(account_number, amount)
            self.assertEqual(str(context.exception), "Amount must be a value greater than zero.")
    
    def test_make_deposit_not_numeric(self):
        """testing ValueError for when input is not float or int"""
        # Arrange
        account_number = "123456"
        amount = "e"
        with patch('builtins.input', side_effect=[account_number, amount]):
            # Act & Assert
            with self.assertRaises(ValueError) as context:
                make_deposit(account_number, amount)
            self.assertEqual(str(context.exception), "Amount must be a numeric type.")
    
    def test_make_deposit_valid(self):
        """Testing valid deposit inputs"""
        # Arrange
        account_number_1 = "123456"

        amount_deposit = "1501.10"

        amount = 1501.10

        account_number = 123456
        
        expected = f"You have made a deposit of {'${:,.2f}'.format(amount)} to account {account_number}"
        
        with patch('builtins.input', side_effect=[account_number_1, amount_deposit]):
            #Act
            result = make_deposit(account_number_1, amount_deposit)

            #Assert
            self.assertEqual(result, expected)

    def test_get_task_invalid_task(self):
        """Testing ValueError exception handling when invalid input is given"""
        # Arrange
        invalid_task = "withdraw"

        with patch('builtins.input', side_effect=["withdraw"]):
            
            # Act & Assert

            with self.assertRaises(ValueError) as context:
                get_task()
            self.assertEqual(str(context.exception), f'"{invalid_task}" is an unknown task.')
            
    def test_get_task_valid_input(self):
        """Testing the parameters of valid inputs, input should not be case sensitive"""
        # Arrange
        valid_input = "balance"

        #Below are two commented out Variables to test alternative inputs
        #valid_input_capital = "BALANCE" 

        #valid_input_mixed = "BalAnCE"
        
        account_number = "123456"

        account_balance = 1000.0

        expected = expected = f"Your current balance for account {account_number} is {'${:,.2f}'.format(account_balance)}"

        with patch('builtins.input', side_effect=[valid_input, account_number]):

            # Act
            result = get_task() 
            
            # Assert
            self.assertEqual(result, expected)