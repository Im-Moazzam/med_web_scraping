import requests
from bs4 import BeautifulSoup


url = "https://www.icd10data.com/ICD10CM/Codes"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
response = requests.get(url,headers=headers)


file_name = f'{url}.html'.replace('https://www.', '').replace('/', '_')

with open(file_name, 'w', encoding='utf-8') as file:
    file.write(response.text)

soup = BeautifulSoup(file_name, 'lxml')

body = soup.find('div', class_ = "body-content")
print(body.prettify())