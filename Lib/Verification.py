import requests
from Lib.Errors import *


class RequestVerification:
    def __init__(self, http: str = '') -> None:
        """
            Проверка адреса на существование или работоспособность
            Запрос адреса может быть выполнен как с ключем API, так и без него
        """
        try:
            if http == '' or 'http' not in http:
                raise HTTPError('HTTPError: Не передан адрес, либо передан некорректно.')

            # Запрос
            response: object = requests.get(http)
            if response.status_code >= 400:
                raise RequestError(response.status_code)
        except RequestError:
            exit()
        except HTTPError:
            exit()


class KeyInDictVerification:
    def __init__(self, item_dict: dict = {}):
        """ Проверка ключей в словарях взятых с hh.ru"""
        # Зарплата от
        pay_f_from: bool = False
        # Зарплата до
        pay_f_to: bool = False
        # Ссылка на вакансию
        url_f: bool = False

        # Проверяем ключи HH.ru
        # Проверка ключей (зп)
        if 'salary' in item_dict and item_dict['salary']:
            # Проверка ключа (зп от)
            if 'from' in item_dict['salary'] and item_dict['salary']['from']:
                pay_f_from = True
            # Проверка ключа (зп до)
            if 'to' in item_dict['salary'] and item_dict['salary']['to']:
                pay_f_to = True
        # Проверка ключа (ссылка на вакансию)
        if 'alternate_url' in item_dict and item_dict['alternate_url']:
            url_f = True

        # Заполняем словарь ключ -> значение(bool)
        self.key_bool_dict: dict = {'pay_from': pay_f_from,
                                    'pay_to': pay_f_to,
                                    'url': url_f}

    @property
    def pay_key_in_dict_verification(self) -> bool:
        """
            :return: Если зп есть в одном из ключей, вернет True
        """
        if self.key_bool_dict['pay_from'] or self.key_bool_dict['pay_to']:
            return True
        return False

    @property
    def get_key_in_dict_verification(self) -> dict:
        """
            :return: словарь key=bool. True - ключ имеет данные
        """
        return self.key_bool_dict
