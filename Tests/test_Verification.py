from Lib.Verification import *
import unittest


class Test_RequestVerification(unittest.TestCase):
    def test_Request_Verification_not_http(self):
        """ Проверка метода без ввода данных """
        with self.assertRaises(SystemExit):
            RequestVerification()

    def test_Request_Verification_http(self):
        """ Проверка метода с неверными данными """
        with self.assertRaises(SystemExit):
            RequestVerification('https://api.superjob.ru/2.0/vacancies/')


class Test_KeyInDictVerification(unittest.TestCase):
    def test_KeyInDictVerification_HH(self):
        """ Проверка метода с верными данными """
        item = {'snippet': {'requirement': 'gfdgfd'}, 'salary': {'from': 999, 'to': 777}, 'alternate_url': 'jghfdj', 'id': 54654}
        HH = KeyInDictVerification(item)
        self.assertEqual(HH.pay_key_in_dict_verification, True)
        self.assertEqual(HH.get_key_in_dict_verification['pay_from'], True)
        self.assertEqual(HH.get_key_in_dict_verification['pay_to'], True)
        self.assertEqual(HH.get_key_in_dict_verification['url'], True)
