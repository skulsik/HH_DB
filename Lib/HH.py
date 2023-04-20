from Lib.Verification import *
import json


class ReadfileJson:
    """ Читает файл с названием компаний работадателя и их id """
    def __init__(self):
        with open('Data/Employers.json', 'r', encoding='UTF-8') as f:
            # Загружаем данные из файла в переменную data
            self.__employers_info: dict = json.load(f)

    @property
    def get_employers_info(self) -> dict:
        """ Возвращает словарь (работадатель: id работадателя) """
        return self.__employers_info


class HH:
    """
        Чтение вакансий работадателей, максимум 100 вакансий от одного работадателя. По умолчанию 10 работадателей.
        Запись работадателей в список, каждому работадателю присвоен список вакансий данного работадателя.
    """
    # Адрес сайта с вакансиями
    http: str = 'https://api.hh.ru/vacancies'

    # Количество вакансий, читаемых за один запрос <=100
    per_page: int = 10

    def __init__(self):
        """ Инициализация свойств(переменных) """
        # Инициализация списка, для формирования списка вакансий
        self.__requests_job_list: list = []

    def add_vacancies_to_list(self, requests_job: dict = {}) -> list:
        """
            Обработка полученного словаря с вакансиями, от работадателя.
            Берет нужную информацию по каждой вакансии, приводит к удобному виду, записывает в список.
        """
        requests_job_list: list = []
        for item in requests_job['items']:
            if 'name' in item:
                # Проверка ключей существование и наличие в них данных
                KIDV: object = KeyInDictVerification(item)
                # Возвращает словарь key=bool. True - ключ имеет данные
                key_bool_dict: dict = KIDV.get_key_in_dict_verification

                # При существовании нужных ключей, приводит к удобному виду для дальнейшей работы, записывает в список
                if KIDV.pay_key_in_dict_verification and key_bool_dict['url']:
                    job_dict: dict = {'name': item['name'],
                                      'from': item['salary']['from'],
                                      'to': item['salary']['to'],
                                      'url': item['alternate_url']}
                    requests_job_list.append(job_dict)
        return requests_job_list

    def get_request(self, name_employer: str = '', id_employer: int = 0) -> None:
        """
            Получает имя работадателя и его id.
            По id работадателя, делает запрос на вакансии данного работадателя(по умолчанию max=100 вакансий)
            Создает словарь('работадатель': 'список вакансий данного работадателя') и добавляет в список.
        """
        # Параметры запроса
        params: dict = {
            'employer_id': f'{str(id_employer)}',
            'per_page': self.per_page,
            'page': 0
        }

        # Временный словарь для хранения запроса(словаря вакансий)
        requests_job: dict = requests.get(self.http, params=params).json()
        # Передает данные из запроса, получает обработанные данные
        requests_job_list: list = self.add_vacancies_to_list(requests_job=requests_job)

        # Добавление в список, словаря ('работадатель': 'список вакансий данного работадателя')
        self.__requests_job_list += [{f'{name_employer}': requests_job_list}]

    def getting_vacancies(self) -> None:
        """ Основной метод для создания списка вакансий, объединяет другие методы класса """
        # Проверка адреса на работаспособность
        RequestVerification(http=self.http)

        # Считывает фаил с работадателями и их id
        rdj: object = ReadfileJson()
        employers_info: dict = rdj.get_employers_info

        # Создает список по каждому работадателю('работадатель': 'список вакансий данного работадателя')
        for name_employer in employers_info:
            self.get_request(name_employer=name_employer, id_employer=employers_info[name_employer])

    @property
    def get_job_list(self) -> list:
        """
            :return: Список вакансий HH.ru
        """
        return self.__requests_job_list
