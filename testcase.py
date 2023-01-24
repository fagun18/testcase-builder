import unittest

class TestSoftware(unittest.TestCase):
    def test_login(self):
        # Test login functionality
        response = login('username', 'password')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

    def test_logout(self):
        # Test logout functionality
        response = logout()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Success')

    def test_create_user(self):
        # Test create user functionality
        response = create_user('John Doe', 'johndoe@example.com', 'password')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'User created')

    def test_update_user(self):
        # Test update user functionality
        response = update_user('John Doe', 'johndoe@example.com', 'newpassword')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'User updated')

    def test_delete_user(self):
        # Test delete user functionality
        response = delete_user('johndoe@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'User deleted')

if __name__ == '__main__':
    unittest.main()
