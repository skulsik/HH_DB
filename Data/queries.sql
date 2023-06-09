CREATE DATABASE hh_vacancy;

CREATE TABLE employers_data (
    employer_id serial PRIMARY KEY,
    name_company varchar(255) NOT NULL
);

CREATE TABLE vacancies_data (
    vacancy_id SERIAL PRIMARY KEY,
    employer_id INTEGER REFERENCES employers_data(employer_id),
    vacancy_name VARCHAR(255),
    salary_from INTEGER,
    salary_to INTEGER,
    url VARCHAR(255)
);

INSERT INTO employers_data (name_company) VALUES ('skyeng');
INSERT INTO employers_data (name_company) VALUES ('skyeng');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (1, 'Куратор образовательных курсов', 0, 60000, 'https://hh.ru/vacancy/78078302');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (1, 'Куратор образовательных курсов', 0, 60000, 'https://hh.ru/vacancy/78198116');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (1, 'Менеджер в онлайн школу удаленно', 0, 100000, 'https://hh.ru/vacancy/78709444');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (1, 'Тренинг специалист', 100000, 130000, 'https://hh.ru/vacancy/79304233');

INSERT INTO employers_data (name_company) VALUES ('LADA');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Водитель - экспедитор автосалон LADA', 30000, 30000, 'https://hh.ru/vacancy/79306941');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Бухгалтер-кассир', 35000, 35000, 'https://hh.ru/vacancy/79670456');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Слесарь по ремонту автомобилей', 80000, 0, 'https://hh.ru/vacancy/79463511');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Специалист по привлечению клиентов', 70000, 70000, 'https://hh.ru/vacancy/78825077');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Специалист по охране труда', 30000, 30000, 'https://hh.ru/vacancy/79428280');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Администратор СТО', 45000, 50000, 'https://hh.ru/vacancy/79517365');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Менеджер по продажам и работе с клиентами', 80000, 0, 'https://hh.ru/vacancy/76853633');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Менеджер / Ассистент Сервисного центра / Администратор / Офис-менеджер', 33500, 38000, 'https://hh.ru/vacancy/78952453');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (2, 'Администратор СТО', 45000, 0, 'https://hh.ru/vacancy/77664423');

INSERT INTO employers_data (name_company) VALUES ('Mechel');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (3, 'Ведущий специалист департамента управления перевозками', 0, 129000, 'https://hh.ru/vacancy/79648242');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (3, 'Электромонтер на завод', 75000, 0, 'https://hh.ru/vacancy/78870474');

INSERT INTO employers_data (name_company) VALUES ('SibAgro');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Специалист по работе с клиентами и договорами', 32500, 53000, 'https://hh.ru/vacancy/78767077');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Заместитель директора по логистике', 150000, 183000, 'https://hh.ru/vacancy/78889879');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Консультант 1С', 56000, 84000, 'https://hh.ru/vacancy/79336019');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Специалист департамента растениеводства', 45000, 52000, 'https://hh.ru/vacancy/79308967');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Продакт-менеджер', 58000, 58000, 'https://hh.ru/vacancy/79079699');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Специалист по работе с клиентами и договорами', 35000, 52000, 'https://hh.ru/vacancy/77648177');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Менеджер оптовых продаж', 52000, 115000, 'https://hh.ru/vacancy/77648330');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (4, 'Аналитик бизнес-процессов', 90000, 147000, 'https://hh.ru/vacancy/76550100');

INSERT INTO employers_data (name_company) VALUES ('TomLesDrev');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Заместитель главного энергетика', 110000, 0, 'https://hh.ru/vacancy/79248811');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Диспетчер-логист', 45000, 0, 'https://hh.ru/vacancy/78546688');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Контролер лесозаготовительного производства', 30000, 45000, 'https://hh.ru/vacancy/78109250');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Заместитель главного энергетика', 110000, 0, 'https://hh.ru/vacancy/79248812');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Ведущий инженер-энергетик (теплоэнергетик)', 80000, 0, 'https://hh.ru/vacancy/79523547');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Водитель автомобиля Тайота Дюна (Манипулятор)', 36000, 0, 'https://hh.ru/vacancy/79254367');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Обмотчик электрических машин и аппаратов', 46000, 0, 'https://hh.ru/vacancy/79638282');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Специалист по охране труда', 51000, 0, 'https://hh.ru/vacancy/78697683');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Водитель автомобиля (Hyunday Gold)', 36000, 0, 'https://hh.ru/vacancy/79195482');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (5, 'Инженер (Производственно-аналитический отдел)', 54500, 0, 'https://hh.ru/vacancy/78666782');

INSERT INTO employers_data (name_company) VALUES ('LeroyMerlin');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (6, 'Сотрудник склада', 40000, 0, 'https://hh.ru/vacancy/79049413');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (6, 'Ночной сотрудник склада', 51000, 58300, 'https://hh.ru/vacancy/79221882');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (6, 'Ночной сотрудник склада', 40300, 0, 'https://hh.ru/vacancy/78838482');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (6, 'Продавец-консультант', 51000, 0, 'https://hh.ru/vacancy/79607748');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (6, 'Администратор по обслуживанию интернет-заказов (МЕГА)', 42900, 0, 'https://hh.ru/vacancy/79400930');

INSERT INTO employers_data (name_company) VALUES ('Mikran');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Электрогазосварщик', 50000, 0, 'https://hh.ru/vacancy/79667061');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Диспетчер', 25000, 0, 'https://hh.ru/vacancy/78716548');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Старший специалист', 35000, 0, 'https://hh.ru/vacancy/78710218');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Подсобный рабочий', 25000, 30000, 'https://hh.ru/vacancy/79600128');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Диспетчер', 30000, 30000, 'https://hh.ru/vacancy/79602649');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Специалист ОМТО', 45000, 60000, 'https://hh.ru/vacancy/78713495');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Специалист технической поддержки 1 линии', 40000, 54000, 'https://hh.ru/vacancy/78890946');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Специалист по договорной деятельности', 40000, 40000, 'https://hh.ru/vacancy/78991498');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (7, 'Инженер', 45000, 0, 'https://hh.ru/vacancy/79575749');

INSERT INTO employers_data (name_company) VALUES ('Auchan');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (8, 'Бизнес-партнер по персоналу (менеджер по персоналу)', 70000, 75000, 'https://hh.ru/vacancy/79637614');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (8, 'Специалист службы безопасности', 34820, 40260, 'https://hh.ru/vacancy/79670883');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (8, 'Специалист службы безопасности', 37660, 49560, 'https://hh.ru/vacancy/79669891');

INSERT INTO employers_data (name_company) VALUES ('RosAtom');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Специалист по рекламационной работе', 75000, 85000, 'https://hh.ru/vacancy/79479556');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Ведущий специалист по мобилизационной работе, гражданской обороне и чрезвычайным ситуациям', 90000, 103000, 'https://hh.ru/vacancy/77231809');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Референт', 56760, 72262, 'https://hh.ru/vacancy/79442379');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Специалист по дизайну', 25000, 30450, 'https://hh.ru/vacancy/79670123');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Монтажник РЭА и приборов', 90000, 0, 'https://hh.ru/vacancy/73815502');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Контролёр радиоэлектронной аппаратуры и приборов', 80000, 90000, 'https://hh.ru/vacancy/79612259');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Руководитель проектов', 90000, 140000, 'https://hh.ru/vacancy/79243449');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Ведущий специалист в коммерческий отдел', 89000, 89000, 'https://hh.ru/vacancy/79263502');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Начальник отдела защиты активов', 140000, 160000, 'https://hh.ru/vacancy/78777247');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (9, 'Регулировщик (радиоэлектронная аппаратура и приборы)', 80000, 0, 'https://hh.ru/vacancy/79055574');

INSERT INTO employers_data (name_company) VALUES ('SochiPark');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Менеджер MICE', 80000, 0, 'https://hh.ru/vacancy/79533037');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Дежурный менеджер', 50655, 60785, 'https://hh.ru/vacancy/79450475');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Кладовщик-приемщик', 48000, 0, 'https://hh.ru/vacancy/79451676');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Помощник оператора аттракционов', 37950, 45540, 'https://hh.ru/vacancy/79172048');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Специалист отдела по управлению сервисом', 46200, 55440, 'https://hh.ru/vacancy/79150911');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Бармен кафе "Волшебный сад"', 45000, 0, 'https://hh.ru/vacancy/79673663');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Оператор складского учета (склад ФК)', 45500, 0, 'https://hh.ru/vacancy/79242931');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Ведущий дизайнер', 63141, 75169, 'https://hh.ru/vacancy/79451097');

INSERT INTO vacancies_data (employer_id, vacancy_name, salary_from, salary_to, url) VALUES (10, 'Менеджер кафе "Чиполлино"', 50000, 0, 'https://hh.ru/vacancy/78523992');

