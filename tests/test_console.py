#!/usr/bin/python3

"""
Unittests for command interpreter
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        self.cmd = None

    def test_quit_command_with_argument(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('quit some_argument'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_EOF_command_success(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd('EOF'))
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')

    def test_emptyline_command(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd('')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
