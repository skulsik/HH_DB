from Lib.HH import HH


def main():
    """ Запуск программы """
    hh: object = HH()
    hh.getting_vacancies()
    list_of_vacancy: list = hh.get_job_list
    for item in list_of_vacancy:
        print(item)


if __name__ == '__main__':
    main()
