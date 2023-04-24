from Lib.DB_Operations import *
import unittest


class Test_Config(unittest.TestCase):
    def test_Config(self):
        """ Проверка метода """
        db: dict = Config.config()
        self.assertEqual(db['user'], 'postgres')


class Test_DB_Operations(unittest.TestCase):
    # Название базы данных
    db_name: str = 'hh_vacancy'
    db = DB_Operations(db_name=db_name)
    def test_sql_request(self):
        """ Проверка метода """
        select_db: bool = self.db.sql_request('SELECT 1;', write_file=True, get_results=True)
        self.assertEqual(select_db[0][0], True)

    def test_checking_table(self):
        """ Проверка метода """
        table: bool = self.db.checking_table('employers_data')
        self.assertEqual(table, True)

    def test_get_all_vacancies(self):
        self.assertEqual(self.db.get_all_vacancies(), None)

    def test_get_companies_and_vacancies_count(self):
        self.assertEqual(self.db.get_companies_and_vacancies_count(), None)

    def test_get_avg_salary(self):
        self.assertEqual(self.db.get_avg_salary(), None)

    def test_get_vacancies_with_higher_salary(self):
        self.assertEqual(self.db.get_vacancies_with_higher_salary(), None)

    def test_get_vacancies_with_keyword(self):
        self.assertEqual(self.db.get_vacancies_with_keyword('python'), None)
