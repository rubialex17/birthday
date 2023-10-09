import unittest
from unittest.mock import patch, Mock
from datetime import date
from app import app
from app.views import get_birthday, save_or_update_birthday, calculate_days, validate_username, validate_date, run_postgres_command 

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @patch('app.views.run_postgres_command') 
    def test_get_birthday(self, mock_run_postgres_command):
        mock_run_postgres_command.return_value = [('1990-01-01',)]

        result = get_birthday('johndoe')

        mock_run_postgres_command.assert_called_once_with("SELECT birthdaydate from birthday where name = 'johndoe'")

        self.assertEqual(result, [('1990-01-01',)])

    @patch('app.views.run_postgres_command')
    def test_save_or_update_birthday(self, mock_run_postgres_command):
        mock_run_postgres_command.return_value = None

        data = {'birthday': '1990-01-01'}
        response = save_or_update_birthday('johndoe', data)

        mock_run_postgres_command.assert_called_once_with("INSERT INTO birthday (name, birthdaydate)\n        VALUES('johndoe','1990-01-01') \n        ON CONFLICT (name) \n        DO \n        UPDATE SET birthdaydate = EXCLUDED.birthdaydate\n        RETURNING id;")

        self.assertEqual(response.status_code, 204)

    def test_calculate_days(self):
        birthday = date.today()
        days = calculate_days(birthday)
        self.assertEqual(days, 0)

    def test_validate_username(self):
        valid_username = "johndoe"
        invalid_username = "1234"
        self.assertTrue(validate_username(valid_username))
        self.assertFalse(validate_username(invalid_username))

    def test_validate_date(self):
        valid_date = "1990-01-01"
        invalid_date = "invalid_date"
        self.assertTrue(validate_date(valid_date))
        self.assertFalse(validate_date(invalid_date))

if __name__ == '__main__':
    unittest.main()





