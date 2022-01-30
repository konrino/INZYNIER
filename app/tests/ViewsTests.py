import requests
import unittest

host = 'http://localhost:5000'


class IntegrationTest(unittest.TestCase):

    def test_integration_roi_endpoint(self):
        response = requests.get(
            host + '/spolka-filter/analiza?spolka_nazwa=ALLEGRO&inwestycja=5000&data_od=2021-10-01&data_do=2021-10-22')
        json_data = response.json()
        self.assertEqual(json_data['spolka'], 'ALlEGRO')
        self.assertEqual(json_data['roi'], '-13.339%')
        self.assertEqual(json_data['kurs_max'], 59.88)
        self.assertEqual(json_data['data_dodania_max'], '10/11/2021')


if __name__ == '__main__':
    unittest.main()
