import psycopg2
from configparser import ConfigParser


class Config:
    """ Чтение данных подключения к БД """
    def config(filename: str = "Data/database.ini", section: str = "postgresql") -> dict:
        # Создает объект
        parser: object = ConfigParser()
        # Читает фаил
        parser.read(filename)
        db: dict = {}
        if parser.has_section(section):
            params: list = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        return db


class SQLWriteToFile:
    """ Запись всех SQL запросов в фаил queries.sql """
    def __init__(self, sql_request: str = ''):
        with open('Data/queries.sql', 'a', encoding='UTF-8') as fail:
            fail.write(f'{sql_request}\n\n')


class FileCleaning:
    def __init__(self):
        """ Очищает фаил от ненужных запросов(при обновлении вакансий, предыдущие запросы могут не соответствовать текущим). """
        with open('Data/queries.sql', 'r+', encoding='UTF-8') as file:
            lines = file.readlines()
            file.seek(0)  # переместить указатель в начало файла
            file.writelines(lines[:17])  # записать первые 17 строк обратно в файл
            file.truncate()


class DB_Operations:
    def __init__(self, db_name: str = '') -> None:
        # Читает database.ini, возвращает словарь с данными
        db_config: dict = Config.config()
        # Определение свойств
        self.db_name: str = db_name
        self.user: str = db_config['user']
        self.password: str = db_config['password']
        self.host: str = db_config['host']
        self.port: str = db_config['port']

    def sql_request(self, sql_request: str = '', write_file: bool = False, get_results: bool = False) -> list:
        """ Выполняет SQL запрос """
        # Список для возврата результатов
        sql_request_result: list = []
        # Соединение с БД
        with psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host, port=self.port) as connection:
            # Создание курсора
            with connection.cursor() as cursor:
                # Отправка запроса в БД, если подразумевается ответ, получает его в переменную
                cursor.execute(sql_request)
                if get_results:
                    sql_request_result = cursor.fetchall()
        connection.close()
        # Запись запроса в фаил
        if write_file:
            SQLWriteToFile(sql_request)
        return sql_request_result

    def creating_db(self) -> None:
        """ Создает БД, если бд с таким именем не существует"""
        connection = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port)
        connection.autocommit = True
        cursor = connection.cursor()
        # Проверка, существует ли уже база данных
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{self.db_name}';")
        exists = cursor.fetchone()

        # Если база данных не существует, то создаем её
        if not exists:
            # sql запрос
            sql_request: str = f'CREATE DATABASE {self.db_name};'
            # Запрос в БД
            cursor.execute(sql_request)
            # Запись запроса в фаил
            SQLWriteToFile(sql_request)
            print(f"DB '{self.db_name}' создана!")
        connection.commit()
        cursor.close()
        connection.close()

    def creating_table(self, table_name: str = '', sql_request: str = '') -> None:
        """ Создает таблицу, если таблица с таким именем не существует"""
        connection = psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host, port=self.port)
        cursor = connection.cursor()
        # Проверка, существует ли таблица
        cursor.execute(f"SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='{table_name}');")
        exists = cursor.fetchone()[0]

        # Если таблица не существует, то создаем её
        if not exists:
            # Запрос в БД
            cursor.execute(sql_request)
            # Запись запроса в фаил
            SQLWriteToFile(sql_request)
            print(f"Таблица '{table_name}' создана!")
        connection.commit()
        cursor.close()
        connection.close()

    def checking_table(self, table_name: str = '') -> bool:
        """
            Проверяет таблицу, на существование в ней данных.
            Возвращает: True - данные существуют; False - таблица пустая
        """
        connection = psycopg2.connect(dbname=self.db_name, user=self.user, password=self.password, host=self.host, port=self.port)
        cursor = connection.cursor()
        # Запрос
        cursor.execute(f"SELECT EXISTS(SELECT 1 FROM {table_name});")
        exists = cursor.fetchone()[0]
        connection.commit()
        cursor.close()
        connection.close()
        return exists

    def writing_data_to_the_database(self, list_of_vacancy: list = []) -> None:
        """ Заполняет таблицу в бд из списка"""
        for index in range(len(list_of_vacancy)):
            # Формирование запроса и наполнение таблицы employers_data
            key: str = list(list_of_vacancy[index].keys())[0]
            sql_request_employers_data: str = f"INSERT INTO employers_data (name_company) VALUES ('{key}');"
            self.sql_request(sql_request=sql_request_employers_data, write_file=True)

            for vacancy in list_of_vacancy[index][key]:
                # Страховка на значения null
                salary_from: int = 0
                salary_to: int = 0
                if vacancy['from']:
                    salary_from = vacancy['from']
                if vacancy['to']:
                    salary_to = vacancy['to']
                # Формирование запроса и наполнение таблицы vacancies_data
                sql_request_vacancies_data: str = f"INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES ({index+1}, '{vacancy['name']}', {salary_from}, {salary_to}, '{vacancy['url']}');"
                self.sql_request(sql_request=sql_request_vacancies_data, write_file=True)

    def get_all_vacancies(self) -> None:
        """ Получает и выводит список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию. """
        sql_request: str = """SELECT ed.name_company, vd.vacancy_name, 
                              CASE 
                              WHEN vd.salary_from IS NOT NULL AND vd.salary_to IS NOT NULL THEN CONCAT(vd.salary_from, ' - ', vd.salary_to)
                              WHEN vd.salary_from IS NOT NULL THEN CONCAT('from ', vd.salary_from)
                              WHEN vd.salary_to IS NOT NULL THEN CONCAT('to ', vd.salary_to)
                              ELSE 'not specified'
                              END as salary_range, 
                              vd.url
                              FROM vacancies_data as vd
                              JOIN employers_data as ed ON ed.employer_id = vd.employer_id;"""
        table_list: list = self.sql_request(sql_request=sql_request, get_results=True)
        print("-----------------------------------------------------------------------------------------------------")
        for line in table_list:
            print(f"Работадатель: {line[0]}")
            print(f"Вакансия: {line[1]}")
            print(f"Зарплата: {line[2]}")
            print(f"Ссылка: {line[3]}")
            print("-----------------------------------------------------------------------------------------------------")

    def get_companies_and_vacancies_count(self) -> None:
        """  Получает список всех компаний и количество вакансий у каждой компании. """
        sql_request: str = """SELECT employers_data.name_company, COUNT(vacancies_data.vacancy_id) as vacancy_count
                              FROM employers_data 
                              JOIN vacancies_data ON employers_data.employer_id = vacancies_data.employer_id
                              GROUP BY employers_data.name_company
                              ORDER BY vacancy_count DESC;"""
        table_list: list = self.sql_request(sql_request=sql_request, get_results=True)
        print("-----------------------------------------------------------------------------------------------------")
        for line in table_list:
            print(f"Работадатель: {line[0]}")
            print(f"Вакансий: {line[1]}")
            print(
                "-----------------------------------------------------------------------------------------------------")

    def get_avg_salary(self) -> None:
        """  Получает среднюю зарплату по вакансиям. """
        sql_request: str = """SELECT v.vacancy_name, AVG((v.salary_from + v.salary_to) / 2) AS avg_salary, v.url
                              FROM vacancies_data v
                              JOIN employers_data e ON v.employer_id = e.employer_id
                              GROUP BY v.vacancy_name, v.url;"""
        table_list: list = self.sql_request(sql_request=sql_request, get_results=True)
        print("-----------------------------------------------------------------------------------------------------")
        for line in table_list:
            print(f"Вакансия: {line[0]}")
            print(f"Зарплата: {int(line[1])}")
            print(f"Ссылка: {line[2]}")
            print(
                "-----------------------------------------------------------------------------------------------------")

    def get_vacancies_with_higher_salary(self) -> None:
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        sql_request: str = """SELECT vacancy_name, salary_from, url
                              FROM vacancies_data
                              WHERE salary_from > (
                                  SELECT AVG(salary_from)
                                  FROM vacancies_data
                              );"""
        table_list: list = self.sql_request(sql_request=sql_request, get_results=True)
        print("-----------------------------------------------------------------------------------------------------")
        for line in table_list:
            print(f"Вакансия: {line[0]}")
            print(f"Зарплата: {int(line[1])}")
            print(f"Ссылка: {line[2]}")
            print(
                "-----------------------------------------------------------------------------------------------------")

    def get_vacancies_with_keyword(self, word: str = '') -> None:
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”. """
        sql_request: str = f"""SELECT v.vacancy_name, v.salary_from, e.name_company, v.url
                               FROM vacancies_data v
                               JOIN employers_data e ON v.employer_id = e.employer_id
                               WHERE v.vacancy_name LIKE '%{word}%';"""
        table_list: list = self.sql_request(sql_request=sql_request, get_results=True)
        print("-----------------------------------------------------------------------------------------------------")
        for line in table_list:
            print(f"Вакансия: {line[0]}")
            print(f"Зарплата: {int(line[1])}")
            print(f"Работадатель: {line[2]}")
            print(f"Ссылка: {line[3]}")
            print(
                "-----------------------------------------------------------------------------------------------------")
