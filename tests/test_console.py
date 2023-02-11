#!/usr/bin/python3
'''
tests for console
'''


import unittest


class TestConsole(unittest.TestCase):
    ''' test cases for console class'''

    def test_docstrings_in_console(self):
        ''' tests for docs'''
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand().do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand().do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand().emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand().do_create.__doc__)
        self.assertIsNotNone(HBNBCommand().do_show.__doc__)
        self.assertIsNotNone(HBNBCommand().do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand().do_all.__doc__)
        self.assertIsNotNone(HBNBCommand().do_update.__doc__)
        self.assertIsNotNone(HBNBCommand().do_count.__doc__)
        self.assertIsNotNone(HBNBCommand().default.__doc__)

if __name__ == '__main__':
    ''' for imports'''
    unittest.main()
