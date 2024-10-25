import unittest
from unittest.mock import patch, MagicMock
import os
import csv
from src.main import (
    check_and_create_directories,
    create_default_config_files,
    is_valid_csv,
    load_csv_to_list,
    enrich_data_with_openai,
    save_to_csv
)

class TestEducauseLeadsEnrichmentService(unittest.TestCase):

    def setUp(self):
        # Setup code to run before each test
        self.test_csv = 'test.csv'
        with open(self.test_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'FirstName', 'LastName', 'Title', 'Company'])
            writer.writerow(['1', 'John', 'Doe', 'Engineer', 'TechCorp'])

    def tearDown(self):
        # Cleanup code to run after each test
        if os.path.exists(self.test_csv):
            os.remove(self.test_csv)

    def test_check_and_create_directories(self):
        check_and_create_directories()
        self.assertTrue(os.path.exists('conf'))
        self.assertTrue(os.path.exists('data'))

    def test_create_default_config_files(self):
        create_default_config_files()
        self.assertTrue(os.path.exists('conf/accounts.csv'))
        self.assertTrue(os.path.exists('conf/categories.csv'))

    def test_is_valid_csv(self):
        self.assertTrue(is_valid_csv(self.test_csv))
        self.assertFalse(is_valid_csv('invalid.txt'))

    def test_load_csv_to_list(self):
        data_list = load_csv_to_list(self.test_csv)
        self.assertEqual(len(data_list), 1)
        self.assertEqual(data_list[0]['FirstName'], 'John')

    @patch('src.main.openai.Completion.create')
    def test_enrich_data_with_openai(self, mock_openai):
        mock_response = MagicMock()
        mock_response.choices = [MagicMock(text='{"Number of Students": "1000", "Recent AI work": "AI Research", "AI link 1": "http://link1.com", "AI link 2": "http://link2.com", "AI link 3": "http://link3.com"}')]
        mock_openai.return_value = mock_response

        data_list = load_csv_to_list(self.test_csv)
        enriched_data = enrich_data_with_openai(data_list)
        self.assertEqual(enriched_data[0]['Number of Students'], '1000')

    def test_save_to_csv(self):
        data = [{'ID': '1', 'firstname': 'John', 'lastname': 'Doe', 'Title': 'Engineer', 'Company': 'TechCorp', 'Number of Students': '1000', 'Recent AI work': 'AI Research', 'AI link 1': 'http://link1.com', 'AI link 2': 'http://link2.com', 'AI link 3': 'http://link3.com'}]
        output_file = 'output.csv'
        save_to_csv(data, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
