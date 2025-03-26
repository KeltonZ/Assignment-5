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
from src.chatbot import get_account_number

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
            #Act $ Arrange
            with self.assertRaises(ValueError) as context:
                get_account_number()
            self.assertEqual(str(context.exception), "Account number entered does not exist.")

    def tests_get_account_number_account_exists(self):
        """"Tests the account validaiton step"""
        # Arrange
        account_exists = 123456
        with patch('builtins.input', side_effect=[str(account_exists)]):
            # Act
            result = get_account_number()
            # Assert
            self.assertEqual(result, account_exists)

    