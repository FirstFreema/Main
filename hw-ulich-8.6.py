import argparse
from classes.engine import Engine

class HH(Engine):
    vacancies_all = []
    vacancies_dicts = []

    def __init__(self, vacancy, vacancies_count):
        self.vacancy = vacancy
        self.vacancies_count = vacancies_count

    def get_request(self):
        url = 'https://api.hh.ru/vacancies'
        vacancies_per_page = 20
        pages_count = self.vacancies_count // vacancies_per_page
        if self.vacancies_count % vacancies_per_page != 0:
            pages_count += 1

        for num in range(pages_count):
            params = {
                'text': self.vacancy,
                'areas': 113,
                'per_page': vacancies_per_page,
                'page': num,
                'only with salary': True
            }
            response = requests.get(url, params=params)
            info = response.json()
            if info is None:
                return "Данные не получены!"
            elif 'errors' in info:
                return info['errors'][0]['value']
            elif info['found'] == 0:
                return "Нет вакансий"
            else:
                for vacancy in info['items']:
                    if vacancy['salary'] is not None and vacancy['salary']['currency'] == 'RUR':
                        vacancy_dict = {
                            'employer': vacancy['employer']['name'],
                            'name': vacancy['name'],
                            'url': vacancy['alternate_url'],
                            'requirement': vacancy['snippet']['requirement'],
                            'salary_from': vacancy['salary']['from'],
                            'salary_to': vacancy['salary']['to']
                        }
                        if vacancy_dict['salary_from'] is None:
                            vacancy_dict['salary_from'] = "не указано"
                        if vacancy_dict['salary_to'] is None:
                            vacancy_dict['salary_to'] = "не указано"
                        self.vacancies_dicts.append(vacancy_dict)

        return self.vacancies_dicts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Парсер вакансий с hh.ru')
    parser.add_argument('vacancy', type=str, help='Название вакансии для поиска')
    parser.add_argument('vacancies_count', type=int, choices=range(20, 201, 20), help='Количество вакансий для просмотра (от 20 до 200 с шагом 20)')
    parser.add_argument('--sort', action='store_true', help='Сортировать вакансии по зарплате')
    parser.add_argument('--sorted_count', type=int, default=10, help='Количество отсортированных вакансий для вывода (по умолчанию 10)')

    args = parser.parse_args()

    hh_parser = HH(args.vacancy, args.vacancies_count)
    vacancies = hh_parser.get_request()

    if args.sort:
        vacancies = sorted(vacancies, key=lambda x: x['salary_from'], reverse=True)

    for vacancy in vacancies[:args.sorted_count]:
        print(vacancy)




# python hh_parser.py "Python developer" 40 --sort --sorted_count 5
