import unittest
from unittest.mock import patch

from accountant import show_all_docs_info, secretary_program_start

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


class MyTestCase(unittest.TestCase):

    # @patch('builtins.input', lambda *args: 'l')
    # def setUp(self) -> None:
    #     secretary_program_start()
    #
    # @patch('builtins.input', lambda *args: 'q')
    # def tearDown(self) -> None:
    #     secretary_program_start()

    def test_info_doc(self):
        doc = show_all_docs_info()
        self.assertListEqual(doc, documents)


if __name__ == '__main__':
    unittest.main()
