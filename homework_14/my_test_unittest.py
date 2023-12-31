import unittest
from user import User


class TestUsersDB(unittest.TestCase):

    def setUp(self):
        self.admin_user = User('Admin', 0, 1)
        self.test_user1 = User('Admin', 0, 1)
        self.test_user2 = User('Other', 1, 1)

    def test_equal(self):
        self.assertEqual(self.admin_user, self.test_user1)

    def test_not_equal(self):
        self.assertFalse(self.admin_user == self.test_user2)

    def test_name_user(self):
        self.assertRaises(ValueError, User, '123', 123)

    def test_id_user(self):
        self.assertRaises(ValueError, User, 'Anybody', 3.14)

    def test_level_user(self):
        self.assertRaises(ValueError, User, 'Anybody', 3, level=8)


if __name__ == '__main__':
    unittest.main(verbosity=2)
