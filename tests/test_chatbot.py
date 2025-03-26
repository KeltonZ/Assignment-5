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
from src.chatbot import get_account_number, get_amount


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
            
            
    