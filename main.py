from Lib.HH import HH
from Lib.DB_Operations import DB_Operations, FileCleaning


def main():
    """ Запуск программы """
    # Название базы данных
    db_name: str = 'hh_vacancy'
    # Создание объекта DB
    db = DB_Operations(db_name=db_name)
    db.creating_db()

    # Запрос на создание таблицы employers_data
    sql_request: str = """CREATE TABLE employers_data (
    employer_id serial PRIMARY KEY,
    name_company varchar(255) NOT NULL
);"""
    db.creating_table(table_name='employers_data', sql_request=sql_request)

    # Запрос на создание таблицы vacancies_data
    sql_request: str = """CREATE TABLE vacancies_data (
    vacancy_id SERIAL PRIMARY KEY,
    employer_id INTEGER REFERENCES employers_data(employer_id),
    vacancy_name VARCHAR(255),
    salary_from INTEGER,
    salary_to INTEGER,
    url VARCHAR(255)
);"""
    db.creating_table(table_name='vacancies_data', sql_request=sql_request)

    # Проверка таблиц на существование в них данных, возращает
    employers_data: bool = db.checking_table(table_name='employers_data')
    vacancies_data: bool = db.checking_table(table_name='vacancies_data')

    # Переменная для передачи команд
    command: str = ''
    # Если таблицы пустые, команда на запрос вакансий и запись их в БД
    if not employers_data and not vacancies_data:
        command = 'update'
        print('Чтение вакансий с HH.ru')
    # Если одна из таблиц пустая, это незапланированное поведение БД. Предложение пересоздать БД.
    elif not employers_data and vacancies_data or employers_data and not vacancies_data:
        print('Ошибка данных в таблицах: Одна из двух таблиц не заполнена, удалите БД и запустите программу заново.')
        exit()

    # Бесконечный цикл интерфейса
    while command != 'exit':
        # Команда update - считывает вакансий с HH.ru и записывает их в БД
        if command == 'update':
            # Запрос вакансий с HH.ru, возврат списка с вакансиями
            hh: object = HH()
            hh.getting_vacancies()
            list_of_vacancy: list = hh.get_job_list

            if employers_data and vacancies_data:
                # Обнуляем таблицы, сбрасываем ключи
                sql_request_restart: str = """ALTER TABLE vacancies_data DROP CONSTRAINT vacancies_data_employer_id_fkey;
                                              TRUNCATE TABLE vacancies_data RESTART IDENTITY;
                                              TRUNCATE TABLE employers_data RESTART IDENTITY;
                                              ALTER TABLE vacancies_data ADD CONSTRAINT vacancies_data_employer_id_fkey FOREIGN KEY(employer_id) REFERENCES employers_data(employer_id);"""
                db.sql_request(sql_request=sql_request_restart)

                # Чистит фаил, от предыдущих запросов
                FileCleaning()
            # Записывем данные в таблицы БД
            db.writing_data_to_the_database(list_of_vacancy)
            # Переводит флаги, на случай обновления вакансий
            employers_data = True
            vacancies_data = True

        # Выводит по умолчанию или по команде
        if command == 'update' or command == 'all_vacancies' or command == '':
            db.get_all_vacancies()

        if command == 'get_companies':
            db.get_companies_and_vacancies_count()

        if command == 'average_salary':
            db.get_avg_salary()

        if command == 'higher_salary':
            db.get_vacancies_with_higher_salary()

        if command == 'vacancies_keyword':
            word: str = input('Введите слово, по которому будет произведен поиск вакансий:')
            db.get_vacancies_with_keyword(word)

        command = input('Команды для работы с программой:\n'
                        'exit - завершить программу.\n'
                        'update - обновить вакансии.\n'
                        'all_vacancies - получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.\n'
                        'get_companies - получает список всех компаний и количество вакансий у каждой компании.\n'
                        'average_salary - получает среднюю зарплату по вакансиям.\n'
                        'higher_salary - получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
                        'vacancies_keyword - получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.\n'
                        'Введите команду:')

if __name__ == '__main__':
    main()
