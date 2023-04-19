# Методы requests
# response.content — возвращает содержимое ответа в байтовом формате.
# response.text — возвращает содержимое ответа в виде строки.
# response.json() — возвращает содержимое ответа в формате JSON и автоматически преобразует его в словарь Python.
# response.ok — возвращает True, если запрос успешен (код состояния HTTP 2xx), и False в противном случае.

import requests

response_1 = requests.get('https://api.github.com')
print(response_1.status_code)
# print(response_1.content)
print(response_1.current_user_url)

url_1 = 'https://api.github.com/search/repositories'
params = {'q': 'python', 'sort': 'stars'}
response_2 = requests.get(url_1, params=params)
# Эквивалентно URL с параметрами
url_1_1 = 'https://api.github.com/search/repositories?q=python&sort=stars'


# Пример использования:

url_2 = 'https://api.github.com/search/repositories'
params = {'q': 'python', 'sort': 'stars'}
response_3 = requests.get(url_2, params=params)


# print(response_3.content)
# b'{"total_count":3204986,"incomplete_results":false,"items":[{"id":83222441, ...

# print(response_3.text)
# {"total_count":3204990,"incomplete_results":false,"items":[{"id":83222441 ...

# print(response_3.json())
# {'total_count': 3204992, 'incomplete_results': False, 'items': [{'id': 83222441, ...

# print(response_3.ok)
# True