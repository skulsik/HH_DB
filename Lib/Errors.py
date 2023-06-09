class Error(Exception):
    """ Глобальная переменная для отлова ошибок """
    NotError: str = ''


class RequestError(Error):
    """
        Ошибка доступа к странице.
        Возвращает переданную ошибку, либо предопределенную
    """
    def __init__(self, *args, **kwargs) -> None:
        # Словарь с ошибками
        error_dict: dict = {4: 'RequestError: Ошибка клиента.', 5: 'RequestError: Ошибка сервера.'}
        self.message: str = error_dict[int(args[0] / 100)] if args else 'RequestError: Неизвестная ошибка.'
        Error.NotError: str = self.message
        print(self.message)


class HTTPError(Error):
    """
        Ошибка переданного адреса.
        Возвращает переданную ошибку, либо предопределенную
    """
    def __init__(self, *args, **kwargs) -> None:
        self.message: str = args[0] if args else 'HTTPError: Неизвестная ошибка.'
        Error.NotError: str = self.message
        print(self.message)
