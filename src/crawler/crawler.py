import requests

url = 'http://www.kinopoisk.ru/'

result = requests.get(url)

with open('test.html', 'w') as output_file:
  output_file.write(result.text.encode('cp1251'))
